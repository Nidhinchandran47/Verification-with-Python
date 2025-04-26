`timescale 1ps/1ps
module full_adder (
    input a,
    input b,
    input cin,
    output sum,
    output cout
);
    assign sum = a ^ b ^ cin;
    assign cout = (a & b) | (cin & (a ^ b));
    `ifdef DUMP_ENABLED
        initial begin
            $dumpfile("dump.vcd");
            $dumpvars(0, full_adder);
        end
    `endif
endmodule
