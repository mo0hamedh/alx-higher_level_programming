ass Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let s = '';
    for (let i = 0; i < this.width; i++) {
      s += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(s);
    }
  }
}

module.exports = Rectangle;
