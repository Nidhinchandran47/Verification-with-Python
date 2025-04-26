import os
import cocotb_test.simulator

def test_full_adder():
    verilog_sources = ["../rtl/full_adder.v"]

    parameters = {}

    extra_compile_args = []
    if os.getenv("WAVE", "0") == "1":
        extra_compile_args.append("-D DUMP_ENABLED")

    cocotb_test.simulator.run(
        verilog_sources=verilog_sources,
        toplevel="full_adder", 
        module="full_adder_tb", 
        sim_build="sim_build", 
        extra_compile_args=extra_compile_args,
        parameters=parameters,
    )

if __name__ == "__main__":
    test_full_adder()
