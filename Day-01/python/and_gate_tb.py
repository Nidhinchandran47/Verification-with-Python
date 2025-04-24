import cocotb 
from cocotb.triggers import Timer

@cocotb.test() 
async def test_and_basic(dut):
    dut._log.info("Starting AND gate test...")

    for a in [0, 1]:
        for b in [0, 1]:
            dut.a.value = a
            dut.b.value = b

            await Timer(1, units='ns')  # Wait for values to propagate

            expected = a & b
            actual = int(dut.c.value)
            dut._log.info(f" Input A = {a}, Input B = {b}, \n Expected = {expected}, Actual = {actual}")

            assert actual == expected, f"Test failed for A={a}, B={b}. Expected {expected}, got {actual}."
    
    dut._log.info("All tests passed!")