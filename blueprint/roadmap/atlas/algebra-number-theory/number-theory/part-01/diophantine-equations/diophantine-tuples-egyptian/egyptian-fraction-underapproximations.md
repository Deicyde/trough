---
declaration: section
origin: cited
lean: EgyptianFraction.IsNondecreasingEgyptian, EgyptianFraction.IsStrictEgyptian, EgyptianFraction.IsNondecreasingUnderapproximation, EgyptianFraction.IsStrictUnderapproximation, EgyptianFraction.IsNondecreasingUnderapproximation.nonempty, EgyptianFraction.IsNondecreasingUnderapproximation.target_pos, EgyptianFraction.IsNondecreasingUnderapproximation.isNondecreasingEgyptian, EgyptianFraction.IsNondecreasingUnderapproximation.denominator_ge_two
statement: formalized
proof: formalized
---

# Egyptian fraction underapproximations

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html).

## Egyptian Fraction

## Nondecreasing Egyptian denominator tuples

A tuple $(a_1, \dots, a_n)$ of natural
numbers lies in $\mathcal{E}_n^{\le}$ when $2 \le a_1 \le a_2 \le \dots \le a_n$, that is, every
$a_i$ is at least $2$ and the tuple is nondecreasing.

## Sources

- Kovač–Tang, arXiv:2607.28387v2, lines 103–107.

Formalized by `EgyptianFraction.IsNondecreasingEgyptian`, a definition declared in [MathlibExt/NumberTheory/EgyptianFraction.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EgyptianFraction.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html#is-nondecreasing-egyptian).

## Strictly increasing Egyptian denominator tuples

A tuple $(a_1, \dots, a_n)$ of natural
numbers lies in $\mathcal{E}_n^{<}$ when $2 \le a_1 < a_2 < \dots < a_n$, that is, every $a_i$ is
at least $2$ and the tuple is strictly increasing.

## Sources

- Kovač–Tang, arXiv:2607.28387v2, lines 108–110.

Formalized by `EgyptianFraction.IsStrictEgyptian`, a definition declared in [MathlibExt/NumberTheory/EgyptianFraction.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EgyptianFraction.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html#is-strict-egyptian).

## Egyptian underapproximations with nondecreasing denominators

Let $\lambda$ be a real
number and $a = (a_1, \dots, a_n)$ a tuple of natural numbers. Then $a$ is a nondecreasing
underapproximation of $\lambda$ when $n \ge 1$, $\lambda > 0$, $a$ lies in
$\mathcal{E}_n^{\le}$ (that is, $2 \le a_1 \le \dots \le a_n$), and
$\sum_{i=1}^{n} 1/a_i < \lambda$, the sum taken in the real numbers.

## Sources

- Kovač–Tang, arXiv:2607.28387v2, lines 113–120; $n \ge 1$ and $\lambda > 0$ follow the paper's conventions.

Formalized by `EgyptianFraction.IsNondecreasingUnderapproximation`, a definition declared in [MathlibExt/NumberTheory/EgyptianFraction.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EgyptianFraction.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html#is-nondecreasing-underapproximation).

## Egyptian underapproximations with strictly increasing denominators

Let $\lambda$ be a
real number and $a = (a_1, \dots, a_n)$ a tuple of natural numbers. Then $a$ is a strict
underapproximation of $\lambda$ when $n \ge 1$, $\lambda > 0$, $a$ lies in $\mathcal{E}_n^{<}$
(that is, $2 \le a_1 < \dots < a_n$, so the unit fractions are distinct), and
$\sum_{i=1}^{n} 1/a_i < \lambda$, the sum taken in the real numbers.

## Sources

- Kovač–Tang, arXiv:2607.28387v2, lines 113–120.

Formalized by `EgyptianFraction.IsStrictUnderapproximation`, a definition declared in [MathlibExt/NumberTheory/EgyptianFraction.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EgyptianFraction.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html#is-strict-underapproximation).

## Nondecreasing underapproximations have at least one term

Let $n$ be a natural number,
$\lambda$ a real number and $a_1, \dots, a_n$ natural numbers. If $(a_1, \dots, a_n)$ is a
nondecreasing underapproximation of $\lambda$, then $n \ge 1$.

Formalized by `EgyptianFraction.IsNondecreasingUnderapproximation.nonempty`, a theorem declared in [MathlibExt/NumberTheory/EgyptianFraction.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EgyptianFraction.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html#nonempty).

## The target of a nondecreasing underapproximation is positive

Let $n$ be a natural
number, $\lambda$ a real number and $a_1, \dots, a_n$ natural numbers. If $(a_1, \dots, a_n)$
is a nondecreasing underapproximation of $\lambda$, then $\lambda > 0$.

Formalized by `EgyptianFraction.IsNondecreasingUnderapproximation.target_pos`, a theorem declared in [MathlibExt/NumberTheory/EgyptianFraction.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EgyptianFraction.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html#target-pos).

## Nondecreasing underapproximations have Egyptian denominator tuples

If
$a = (a_1, \dots, a_n)$ is a nondecreasing underapproximation of a real number $\lambda$, then
$a$ lies in $\mathcal{E}_n^{\le}$, that is, $2 \le a_1 \le \dots \le a_n$.

Formalized by `EgyptianFraction.IsNondecreasingUnderapproximation.isNondecreasingEgyptian`, a theorem declared in [MathlibExt/NumberTheory/EgyptianFraction.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EgyptianFraction.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html#is-nondecreasing-egyptian-2).

## Denominators of a nondecreasing underapproximation are at least two

Let $n$ be a
natural number, $\lambda$ a real number and $a_1, \dots, a_n$ natural numbers. If
$(a_1, \dots, a_n)$ is a nondecreasing underapproximation of $\lambda$, then $a_i \ge 2$ for
every $1 \le i \le n$.

Formalized by `EgyptianFraction.IsNondecreasingUnderapproximation.denominator_ge_two`, a theorem declared in [MathlibExt/NumberTheory/EgyptianFraction.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EgyptianFraction.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html#denominator-ge-two).

## Denominators of a nondecreasing underapproximation are nondecreasing

Let $n$ be a
natural number, $\lambda$ a real number and $a_1, \dots, a_n$ natural numbers. If
$(a_1, \dots, a_n)$ is a nondecreasing underapproximation of $\lambda$, then $a_i \le a_j$
whenever $1 \le i \le j \le n$.

Formalized by `EgyptianFraction.IsNondecreasingUnderapproximation.monotone`, a theorem declared in [MathlibExt/NumberTheory/EgyptianFraction.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EgyptianFraction.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html#monotone).

## A nondecreasing underapproximation stays below its target

Let $n$ be a natural number,
$\lambda$ a real number and $a_1, \dots, a_n$ natural numbers. If $(a_1, \dots, a_n)$ is a
nondecreasing underapproximation of $\lambda$, then $\sum_{i=1}^{n} 1/a_i < \lambda$.

Formalized by `EgyptianFraction.IsNondecreasingUnderapproximation.sum_lt`, a theorem declared in [MathlibExt/NumberTheory/EgyptianFraction.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EgyptianFraction.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html#sum-lt).

## Strict underapproximations have at least one term

Let $n$ be a natural number,
$\lambda$ a real number and $a_1, \dots, a_n$ natural numbers. If $(a_1, \dots, a_n)$ is a
strict underapproximation of $\lambda$, then $n \ge 1$.

Formalized by `EgyptianFraction.IsStrictUnderapproximation.nonempty`, a theorem declared in [MathlibExt/NumberTheory/EgyptianFraction.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EgyptianFraction.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html#nonempty-2).

## The target of a strict underapproximation is positive

Let $n$ be a natural number,
$\lambda$ a real number and $a_1, \dots, a_n$ natural numbers. If $(a_1, \dots, a_n)$ is a
strict underapproximation of $\lambda$, then $\lambda > 0$.

Formalized by `EgyptianFraction.IsStrictUnderapproximation.target_pos`, a theorem declared in [MathlibExt/NumberTheory/EgyptianFraction.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EgyptianFraction.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html#target-pos-2).

## Strict underapproximations have strictly increasing Egyptian denominators

If
$a = (a_1, \dots, a_n)$ is a strict underapproximation of a real number $\lambda$, then $a$ lies
in $\mathcal{E}_n^{<}$, that is, $2 \le a_1 < \dots < a_n$.

Formalized by `EgyptianFraction.IsStrictUnderapproximation.isStrictEgyptian`, a theorem declared in [MathlibExt/NumberTheory/EgyptianFraction.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EgyptianFraction.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html#is-strict-egyptian-2).

## Denominators of a strict underapproximation are at least two

Let $n$ be a natural
number, $\lambda$ a real number and $a_1, \dots, a_n$ natural numbers. If $(a_1, \dots, a_n)$
is a strict underapproximation of $\lambda$, then $a_i \ge 2$ for every $1 \le i \le n$.

Formalized by `EgyptianFraction.IsStrictUnderapproximation.denominator_ge_two`, a theorem declared in [MathlibExt/NumberTheory/EgyptianFraction.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EgyptianFraction.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html#denominator-ge-two-2).

## Denominators of a strict underapproximation increase strictly

Let $n$ be a natural
number, $\lambda$ a real number and $a_1, \dots, a_n$ natural numbers. If $(a_1, \dots, a_n)$
is a strict underapproximation of $\lambda$, then $a_i < a_j$ whenever $1 \le i < j \le n$.

Formalized by `EgyptianFraction.IsStrictUnderapproximation.strictMono`, a theorem declared in [MathlibExt/NumberTheory/EgyptianFraction.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EgyptianFraction.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html#strict-mono).

## A strict underapproximation stays below its target

Let $n$ be a natural number,
$\lambda$ a real number and $a_1, \dots, a_n$ natural numbers. If $(a_1, \dots, a_n)$ is a
strict underapproximation of $\lambda$, then $\sum_{i=1}^{n} 1/a_i < \lambda$, the sum taken in
the real numbers.

Formalized by `EgyptianFraction.IsStrictUnderapproximation.sum_lt`, a theorem declared in [MathlibExt/NumberTheory/EgyptianFraction.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EgyptianFraction.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html#sum-lt-2).

## Strict underapproximations are nondecreasing underapproximations

Let $n$ be a natural
number, $\lambda$ a real number and $a_1, \dots, a_n$ natural numbers. If $(a_1, \dots, a_n)$
is a strict underapproximation of $\lambda$, then it is also a nondecreasing
underapproximation of $\lambda$.

This is the inclusion of strictly increasing denominator tuples among nondecreasing ones,
together with the same bound on the sum of reciprocals.

Formalized by `EgyptianFraction.IsStrictUnderapproximation.toIsNondecreasingUnderapproximation`, a theorem declared in [MathlibExt/NumberTheory/EgyptianFraction.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EgyptianFraction.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html#to-is-nondecreasing-underapproximation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Egyptian fraction underapproximations](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/egyptian-fraction-underapproximations)
