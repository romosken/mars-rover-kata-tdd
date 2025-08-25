const DirectionsMap = {
  N: { L: "W", R: "E", AXIS: "y", INCREMENT: 1 },
  E: { L: "N", R: "S", AXIS: "x", INCREMENT: 1 },
  S: { L: "E", R: "W", AXIS: "y", INCREMENT: -1 },
  W: { L: "S", R: "N", AXIS: "x", INCREMENT: -1 },
};

export class Rover {
  direction: string;
  coordinate: object;
  maxIndex: number;
  minIndex: number;

  constructor() {
    this.direction = "N";
    this.maxIndex = 9;
    this.minIndex = 0;

    this.coordinate = {
      x: this.minIndex,
      y: this.minIndex,
    };
  }

  execute(command: string) {
    for (const char of command) {
      if (char === "M") this.move();
      if (char === "R" || char === "L") this.turn(char);
    }
    return `${this.coordinate['x']}:${this.coordinate['y']}:${this.direction}`;
  }

  private move() {
    const currentDirectionMap = DirectionsMap[this.direction];
    const axis = currentDirectionMap["AXIS"];
    const increment = currentDirectionMap["INCREMENT"];
    const current = this.coordinate[axis];
    const next = this.getNextPosition(current, increment);

    this.coordinate[axis] = next;
  }

  private getNextPosition(current, increment: number) {
    const next = current + increment;
    if (next > this.maxIndex) return this.minIndex;
    if (next < this.minIndex) return this.maxIndex;
    return next;
  }

  private turn(char: string) {
    const currentDirectionMap = DirectionsMap[this.direction];
    this.direction = currentDirectionMap[char];
  }
}
