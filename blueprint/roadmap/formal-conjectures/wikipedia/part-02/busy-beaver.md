---
declaration: theorem
origin: cited
lean: BusyBeaver.BB_2, BusyBeaver.BB_3, BusyBeaver.BB_4, BusyBeaver.BB_5, BusyBeaver.BB_6
statement: formalized
---

# Busy Beaver

> The Busy Beaver problem asks for the maximum number of steps that an n-state, 2-symbol Turing
> machine can take before halting, when started on an empty tape.
>
> *References:*
>
> - [The Busy Beaver Challenge](https://wiki.bbchallenge.org/wiki/Main_Page)

*Quoted from [FormalConjectures/Wikipedia/BusyBeaver.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BusyBeaver.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 1 open, 1 solved and 3 textbook results. It also has 1 test statement and 1 API statement, counted here but not shown.

## `BusyBeaver.BB_2`

Textbook result, stated without proof.

> The value of the Busy Beaver function for 2 states is 6.

```lean
theorem BB_2 : BB 2 = 6
```

Category `textbook`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/Wikipedia/BusyBeaver.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BusyBeaver.lean#L79).

## `BusyBeaver.BB_3`

Textbook result, stated without proof.

> The value of the Busy Beaver function for 3 states is 21.

```lean
theorem BB_3 : BB 3 = 21
```

Category `textbook`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/Wikipedia/BusyBeaver.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BusyBeaver.lean#L84).

## `BusyBeaver.BB_4`

Textbook result, stated without proof.

> The value of the Busy Beaver function for 4 states is 107.

```lean
theorem BB_4 : BB 4 = 107
```

Category `textbook`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/Wikipedia/BusyBeaver.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BusyBeaver.lean#L89).

## `BusyBeaver.BB_5`

Solved: stated here without proof.

> The value of the Busy Beaver function for 5 states is 47176870.

```lean
theorem BB_5 : BB 5 = 47176870
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/Wikipedia/BusyBeaver.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BusyBeaver.lean#L94).

## `BusyBeaver.BB_6`

Open: stated without proof.

> Determine the value of the Busy Beaver function at n = 6.

```lean
theorem BB_6 : BB 6 = BB_6.answer
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/Wikipedia/BusyBeaver.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BusyBeaver.lean#L103).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/BusyBeaver.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BusyBeaver.lean)
- [The Busy Beaver Challenge](https://wiki.bbchallenge.org/wiki/Main_Page)
