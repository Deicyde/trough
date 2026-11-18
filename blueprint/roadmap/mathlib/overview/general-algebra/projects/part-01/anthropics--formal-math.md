---
declaration: theorem
origin: cited
lean: Light.Meets.main, Light.Sec4.Answered.all, ThreeSumApsp.lemma_6
statement: formalized
proof: formalized
---

# formal-math

[anthropics/formal-math](https://github.com/anthropics/formal-math) at commit [16a5ce41](https://github.com/anthropics/formal-math/tree/16a5ce41304fcdaea4e0be7c132e1c361dc26da5), 2026-10-27.

> Machine-checked Lean 4 formalizations published by Anthropic. Each subdirectory is a self-contained Lake project with its own toolchain pin, README and build instructions; build from inside the subdirectory. Projects follow the layout of the [Palomar](https://palomar-registry.org/) submission template (`Challenge.lean` / `Solution.lean` / `comparator.json` / `formalization.yaml` at the project root) and are submitted to Palomar with the subdirectory as the selected project; the licence file Palomar reads is this repository's root `LICENSE`.

*Quoted from [README.md](https://github.com/anthropics/formal-math/blob/16a5ce41304fcdaea4e0be7c132e1c361dc26da5/README.md), Apache-2.0.*

## Depends on

Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site.

## Proof depends on

- [Congruence in $\Z$](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md)
- [Finite](../../../combinatorics/pigeonhole-principles/finite.md)
- [Formula for the Number of Combinations](../../../../hundred-theorems/part-03/formula-for-the-number-of-combinations.md)
- [The Binomial Theorem](../../../../hundred-theorems/part-02/the-binomial-theorem.md)
- [Sum of an arithmetic series](../../../../hundred-theorems/part-03/sum-of-an-arithmetic-series.md)
- [Prime numbers](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)
- [Ordered ring](../../rings/ordered-ring.md)
- [Logarithm](../../../analysis/special-functions/logarithm.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`Light.Meets.main`](https://github.com/anthropics/formal-math/blob/16a5ce41304fcdaea4e0be7c132e1c361dc26da5/3sum-apsp/ThreeSumApsp/Lang/ToMachine.lean#L82) (theorem)
- [`Light.Sec4.Answered.all`](https://github.com/anthropics/formal-math/blob/16a5ce41304fcdaea4e0be7c132e1c361dc26da5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Offline.lean#L66) (theorem)
- [`ThreeSumApsp.lemma_6`](https://github.com/anthropics/formal-math/blob/16a5ce41304fcdaea4e0be7c132e1c361dc26da5/3sum-apsp/ThreeSumApsp/Sec2/Lemma6.lean#L188) (theorem)

No file its headlines import, directly or not (67 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.33.1, Mathlib at [0df444a3](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).
- 1,812 .lean files; its Lean libraries `EndStatement`, `PaperStatements`, `ThreeSumApsp`, `Challenge`, `Solution` hold 433, declaring 8,570 names, with `sorry` in 2 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/anthropics/formal-math/blob/16a5ce41304fcdaea4e0be7c132e1c361dc26da5/LICENSE)).

## Builds on

- Mathlib, at [0df444a3](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).

## Placement

Of its imports of Mathlib modules in an overview area, 85 of 148 are in General algebra, 1.6 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: General algebra (85 of 148 imports, 1.6×), Data structures (23 of 148 imports, 1.1×), Analysis (25 of 148 imports, 0.6×). *Proof depends on* names 8 of the 35 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [anthropics/formal-math at 16a5ce41](https://github.com/anthropics/formal-math/tree/16a5ce41304fcdaea4e0be7c132e1c361dc26da5)
