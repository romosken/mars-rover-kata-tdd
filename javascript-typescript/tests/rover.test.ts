import { Rover } from "../src/rover";

describe("testing rover", () => {
  describe("rover creation", () => {
    test("validando que ao criar o rover, ele aponta para 0:0:N", () => {
      const rover = new Rover();
      const expected = "0:0:N";
      const actual = rover.execute("");

      expect(actual).toEqual(expected);
    });
  });

  describe("rover rotation", () => {
    test.each([
      ["R", "0:0:E"],
      ["RR", "0:0:S"],
      ["RRR", "0:0:W"],
      ["RRRR", "0:0:N"],
    ])(
      "checking turning right, command: %s | expected result: %s",
      (command, expected) => {
        const rover = new Rover();
        const actual = rover.execute(command);

        expect(actual).toEqual(expected);
      }
    );

    test.each([
      ["L", "0:0:W"],
      ["LL", "0:0:S"],
      ["LLL", "0:0:E"],
      ["LLLL", "0:0:N"],
    ])(
      "checking turning left, command: %s | expected result: %s",
      (command, expected) => {
        const rover = new Rover();
        const actual = rover.execute(command);

        expect(actual).toEqual(expected);
      }
    );
  });

  describe("rover movement", () => {
    test.each([
      ["MM", "0:2:N"],
      ["MMMMMMMMMM", "0:0:N"],
    ])(
      "checking moving forward, command: %s | expected result: %s",
      (command, expected) => {
        const rover = new Rover();
        const actual = rover.execute(command);

        expect(actual).toEqual(expected);
      }
    );

    test.each([
      ["RMM", "2:0:E"],
      ["RMMMMMMMMMM", "0:0:E"],
      ["RRMM", "0:8:S"],
      ["RRMMMMMMMMMM", "0:0:S"],
      ["RRRMM", "8:0:W"],
      ["RRRMMMMMMMMMM", "0:0:W"],
      ["MMRMMLM", "2:3:N"],
    ])(
      "checking turning and moving, command: %s | expected result: %s",
      (command, expected) => {
        const rover = new Rover();
        const actual = rover.execute(command);

        expect(actual).toEqual(expected);
      }
    );
  });
});
