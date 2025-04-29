import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.clock import Clock

@cocotb.test()
async def test_counter(dut):
    dut._log.info("Starting counter test...")
    clock = Clock(dut.clk, 10, units="ns") 
    cocotb.start_soon(clock.start())

    dut.reset.value = 1
    dut.enable.value = 0
    dut.mode.value = 0
    dut.load.value = 0
    dut.load_value.value = 0
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    assert dut.count.value == 0, f"Counter should be 0 after reset, but got {dut.count.value}"
    
    dut.reset.value = 0
    dut.enable.value = 1
    for i in range(5):
        await RisingEdge(dut.clk)
        await Timer(1, units="ns")
        assert dut.count.value == i + 1, f"Counter should be {i + 1}, but got {dut.count.value}"
    
    dut.load_value.value = 9
    dut.load.value = 1
    await RisingEdge(dut.clk)
    dut.load.value = 0
    await Timer(1, units="ns")
    assert dut.count.value == 9, f"Counter should be loaded with 9, but got {dut.count.value}"
    await RisingEdge(dut.clk)

    dut.mode.value = 1
    for i in range(12):
        await RisingEdge(dut.clk)
        dut._log.info(f"count = {dut.count.value}")
    
    dut._log.info(f"Counter width is: {dut.count.value.n_bits}")
    dut._log.info("Test Completed...")
