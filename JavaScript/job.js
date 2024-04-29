const x = 2;
let y = 4;
function update(arg, arg2) {
  return Math.random() + arg2 * arg;
}
y = 2;
y = 3;
const result = update(x);
console.log(result);

module.exports = {
  update,
};
