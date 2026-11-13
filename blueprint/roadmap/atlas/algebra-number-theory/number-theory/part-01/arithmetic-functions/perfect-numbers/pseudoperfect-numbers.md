---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.DivisorSumReciprocalConvergenceWanted.InA, MathlibExt.NumberTheory.DivisorSumReciprocalConvergenceWanted.conjecture, MathlibExt.NumberTheory.DivisorSumReciprocalConvergenceWanted.conjecture_holds, MathlibExt.NumberTheory.ErdosProblem825Wanted.conjecture, MathlibExt.NumberTheory.ErdosProblem825Wanted.conjecture_holds
statement: formalized
---

# Pseudoperfect numbers

5 results, 3 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/pseudoperfect-numbers/index.html).

## Primitive pseudoperfect numbers

A natural number $n$ lies in $A$, the set of primitive
pseudoperfect numbers, when $n > 0$, $n$ is pseudoperfect (it is positive and equal to the sum of
some set of distinct proper divisors of itself), and no proper divisor of $n$ (a divisor
$m \mid n$ with $m < n$) is pseudoperfect.

Formalized by `MathlibExt.NumberTheory.DivisorSumReciprocalConvergenceWanted.InA`, a definition declared in [WantedExt/NumberTheory/DivisorSumReciprocalConvergenceWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorSumReciprocalConvergenceWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/pseudoperfect-numbers/index.html#in-a).

## Erdős Problem 469 (statement)

The proposition that the reciprocals of the primitive
pseudoperfect numbers have finite sum: the family $(1/n)$, indexed by the natural numbers $n$
that are primitive pseudoperfect, is summable in $\mathbb{R}$. Here $n$ is pseudoperfect if
$n > 0$ and $n$ is the sum of some set of distinct proper divisors of $n$, and primitive
pseudoperfect if moreover no proper divisor of $n$ is pseudoperfect.

## Sources

- [EP-469].

Formalized by `MathlibExt.NumberTheory.DivisorSumReciprocalConvergenceWanted.conjecture`, a definition declared in [WantedExt/NumberTheory/DivisorSumReciprocalConvergenceWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorSumReciprocalConvergenceWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/pseudoperfect-numbers/index.html#conjecture).

## Reciprocals of primitive pseudoperfect numbers have finite sum

Call a natural number
$n$ pseudoperfect if $n > 0$ and $n$ is the sum of some set of distinct proper divisors of $n$,
and primitive pseudoperfect if moreover no proper divisor of $n$ is pseudoperfect. Then the
family $(1/n)$, indexed by the primitive pseudoperfect numbers $n$, is summable in $\mathbb{R}$,
that is, the sum of $1/n$ over all primitive pseudoperfect numbers $n$ is finite.

This is Erdős Problem 469, resolved true.

## Sources

- plby/lean-proofs (2026), https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos469.lean.

Stated but not proved: `MathlibExt.NumberTheory.DivisorSumReciprocalConvergenceWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorSumReciprocalConvergenceWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisorSumReciprocalConvergenceWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/pseudoperfect-numbers/index.html#conjecture-holds).

## Erdős Problem 825

Write $\sigma(n)$ for the sum of the positive divisors of a positive
integer $n$, and call $n$ pseudoperfect if $n$ is the sum of the elements of some set of proper
divisors of $n$. The statement is the conjunction of two claims: there is a real $C > 0$ such
that every positive integer $n$ with $\sigma(n) > Cn$ is pseudoperfect, and every real $C > 0$
with this property satisfies $C > 2$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem825Wanted.conjecture`, a definition declared in [WantedExt/NumberTheory/ErdosProblem825Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem825Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/pseudoperfect-numbers/index.html#conjecture-2).

## Erdős Problem 825 is true

Write $\sigma(n)$ for the sum of the positive divisors of a
positive integer $n$, and call $n$ pseudoperfect if $n$ is the sum of the elements of some set
of proper divisors of $n$. Then there is a real $C > 0$ such that every positive integer $n$
with $\sigma(n) > Cn$ is pseudoperfect, and every real $C > 0$ with this property satisfies
$C > 2$.

## Sources

- Daniel Larsen, Sufficiently abundant numbers are pseudoperfect, https://github.com/Larsen-Daniel/Erdos-825/blob/18411fce83ce49ee0adbb628de04603e003004f5/825.pdf.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem825Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem825Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem825Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/pseudoperfect-numbers/index.html#conjecture-holds-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pseudoperfect numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/pseudoperfect-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/pseudoperfect-numbers)
