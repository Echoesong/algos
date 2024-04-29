const { update } = require("./job");

i = 0;
while (i < 100) {
  test("number should return between 6 and 7", () => {
    output = update(2, 3);
    expect(output).toBeGreaterThan(6);
    expect(output).toBeLessThan(7);
  });
  i++;
}
