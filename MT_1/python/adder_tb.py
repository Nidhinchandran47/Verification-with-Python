import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def adder(dut):
    dut._log.info("Starting ADDER TEST...")

    for X in [0,1]:
        for Y in [0,1]:
            dut.A.value = X
            dut.B.value = Y

            await Timer(10,units='ns')

            expected_sum = X ^ Y
            expected_C = X & Y

            assert dut.SUM == expected_sum, f"SUM Mismatch : {dut.SUM} != {expected_sum}"
            assert dut.C == expected_C, f"C Mismatch : {dut.C} != {expected_C}"
    dut._log.info("All tests Passed")   

