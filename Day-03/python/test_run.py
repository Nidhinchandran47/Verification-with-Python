import os
import cocotb_test.simulator

def test_d_ff():
    verilog_sources = ["../rtl/d_ff.v"]

    parameters = {}

    extra_compile_args = []
    if os.getenv("WAVE", "0") == "1":
        extra_compile_args.append("-D DUMP_ENABLED")

    cocotb_test.simulator.run(
        verilog_sources=verilog_sources,
        toplevel="d_ff", 
        module="d_ff_tb", 
        sim_build="sim_build", 
        compile_args=extra_compile_args,
        parameters=parameters,
    )

if __name__ == "__main__":
    test_d_ff()
