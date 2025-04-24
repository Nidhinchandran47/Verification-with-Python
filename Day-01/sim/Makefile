VERILOG_SOURCE     = ../rtl/and_gate.v
SV_TESTBENCH       = ../verilog/and_gate_tb.v
PYTHON_PATH        = ../python
TOPLEVEL           = and_gate
MODULE             = and_gate_tb
TOPLEVEL_LANG     ?= verilog
SIM               ?= icarus

help:
	@echo "Makefile for $(MODULE)"
	@echo "Usage:"
	@echo "  make clean      - Clean up generated files"
	@echo "  make cocotb     - Run cocotb python testbench"
	@echo "  make sv         - Run SystemVerilog testbench"

cocotb:
	@echo "Running cocotb testbench..."

	PYTHONPATH=$(PYTHON_PATH) \
	$(MAKE) -f $(shell cocotb-config --makefiles)/Makefile.sim \
		SIM=$(SIM) \
		TOPLEVEL_LANG=$(TOPLEVEL_LANG) \
		TOPLEVEL=$(TOPLEVEL) \
		MODULE=$(MODULE) \
		VERILOG_SOURCES="$(abspath $(VERILOG_SOURCE))"

sv:
	@echo "Running SystemVerilog testbench..."
	iverilog -o simv $(VERILOG_SOURCE) $(SV_TESTBENCH) 
	vvp simv

clean:
	rm -rf simv *.vcd *.xml *.f *.log *.out __pycache__ test/__pycache__ *.fst sim_build
	
.PHONY: cocotb sv clean help