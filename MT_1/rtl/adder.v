module adder (
    input A,
    input B,
    output C,
    output SUM
);

assign C = A & B;
assign SUM = A ^ B;


initial begin
    $dumpfile("dump.vcd");
    $dumpvars(0, adder);
end


endmodule