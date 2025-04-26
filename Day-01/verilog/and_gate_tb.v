`timescale 1ns/1ps
module and_gate_tb ();
    reg a, b;
    wire c;
    and_gate dut (
        .a(a),
        .b(b),
        .c(c)
    );
    initial begin
        a = 0; b = 0;
        #10;
        if (c !== 0) $display("Test case 1 failed: expected c = 0, got c = %b", c);
        else $display("Test case 1 passed: expected c = 0, got c = %b", c);

        a = 0; b = 1;
        #10;
        if (c !== 0) $display("Test case 2 failed: expected c = 0, got c = %b", c);
        else $display("Test case 2 passed: expected c = 0, got c = %b", c);

        a = 1; b = 0;
        #10;
        if (c !== 0) $display("Test case 3 failed: expected c = 0, got c = %b", c);
        else $display("Test case 3 passed: expected c = 0, got c = %b", c);

        a = 1; b = 1;
        #10;
        if (c !== 1) $display("Test case 4 failed: expected c = 1, got c = %b", c);
        else $display("Test case 4 passed: expected c = 1, got c = %b", c);

        $finish;
    end
endmodule
