`timescale 1ps/1ps
module full_adder_tb();
    reg a, b, cin;
    wire sum, cout;

    full_adder u_full_adder (
    .a       (a),
    .b       (b),
    .cin     (cin),
    .sum     (sum),
    .cout    (cout)
);
    initial begin
        a = 0; b = 0; cin = 0;
        #10;
        a = 0; b = 0; cin = 1;
        #10;
        a = 0; b = 1; cin = 0;
        #10;
        a = 0; b = 1; cin = 1;
        #10;
        a = 1; b = 0; cin = 0;
        #10;
        a = 1; b = 0; cin = 1;
        #10;
        a = 1; b = 1; cin = 0;
        #10;
        a = 1; b = 1; cin = 1;
        #10;
    end

    initial begin
        $dumpfile("dump.vcd");
        $dumpvars(0, full_adder_tb);
    end

endmodule
