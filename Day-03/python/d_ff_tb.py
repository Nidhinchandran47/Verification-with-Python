import cocotb
from cocotb.triggers import RisingEdge, FallingEdge, Timer

async def clock_gen(dut):
    while True:
        dut.clk.value = 0
        await Timer(5, units="ns")
        dut.clk.value = 1
        await Timer(5, units="ns")

@cocotb.test()
async def test_d_ff_tb(dut):
    dut._log.info("Starting D Flip-Flop test...")
    cocotb.start_soon(clock_gen(dut))

    dut.reset.value = 0
    dut.d.value = 0
    await RisingEdge(dut.clk)
    dut.reset.value = 1
    await RisingEdge(dut.clk)
    assert dut.q.value == 0, f"Q should be 0 after reset, but got {dut.q.value}"

    dut.d.value = 1 
    await RisingEdge(dut.clk)  
    await Timer(1, units="ns")
    assert dut.q.value == 1, f"Q should be 1 after D=1, but got {dut.q.value}"

    await Timer(25, units='ns')
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    assert dut.q.value == 0, f"Reset failed"

    dut._log.info("Test completed")
