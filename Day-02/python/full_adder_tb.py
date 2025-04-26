import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_full_adder(dut):
    dut._log.info("Starting full adder test...")

    for a in [0,1]:
        for b in [0,1]:
            for cin in [0,1]:
                dut.a.value = a
                dut.b.value = b
                dut.cin.value = cin

                await Timer(10, units='ns')

                expected_sum = (a + b + cin) % 2
                expected_cout = (a + b + cin) // 2

                assert dut.sum == expected_sum, f"Sum mismatch: {dut.sum} != {expected_sum}"
                assert dut.cout == expected_cout, f"Cout mismatch: {dut.cout} != {expected_cout}"
    dut._log.info("All tests passed!")
    