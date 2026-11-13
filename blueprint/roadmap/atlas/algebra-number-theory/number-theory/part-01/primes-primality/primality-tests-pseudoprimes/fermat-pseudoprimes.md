---
declaration: section
origin: cited
lean: MetaMathlibExt.cipolla_pseudoprime_construction, MathlibExt.NumberTheory.NonSquarefreeBaseTwoPseudoprimeWanted.conjecture, MathlibExt.NumberTheory.NonSquarefreeBaseTwoPseudoprimeWanted.conjecture_holds
statement: formalized
---

# Fermat pseudoprimes

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/fermat-pseudoprimes/index.html).

## Cipolla's pseudoprime construction

Let $a > 1$ be a natural number and let $p$ be a
prime that does not divide $a(a^2 - 1)$. Put $n_1 = (a^p - 1)/(a - 1)$,
$n_2 = (a^p + 1)/(a + 1)$ and $n = n_1 n_2$. Then $n$ is a Fermat pseudoprime to base $a$:
$n > 1$, $n$ is not prime, and $n$ divides $a^{n-1} - 1$.

## Sources

- Y. Hamahata and Y. Kokubun, "Cipolla Pseudoprimes", Journal of Integer Sequences 10 (2007), Theorem 1 (Cipolla, cf. Ribenboim), lines 87--95, <https://cs.uwaterloo.ca/journals/JIS/VOL10/Hamahata2/hamahata44.tex>.

Formalized by `MetaMathlibExt.cipolla_pseudoprime_construction`, a theorem declared in [MathlibExt/NumberTheory/CipollaPseudoprime.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/CipollaPseudoprime.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/fermat-pseudoprimes/index.html#cipolla-pseudoprime-construction).

## Guy's question on non-squarefree base-two pseudoprimes beyond $10^{13}$

The statement
that there is a natural number $n > 10^{13}$ that is a Fermat pseudoprime to base $2$ (a
composite number $n > 1$ with $n \mid 2^{n-1} - 1$) and is not squarefree.

Guy reports 54 non-squarefree base-two pseudoprimes up to $10^{13}$, all multiples of $1093^2$ or
$3511^2$, and asks whether there are any other "square psp"s. Here "square psp" means a
non-squarefree base-two pseudoprime, not a number that is itself a perfect square. Guy poses this
as a question; this is its affirmative existence form, which does not predict the answer.

Formalized by `MathlibExt.NumberTheory.NonSquarefreeBaseTwoPseudoprimeWanted.conjecture`, a definition declared in [WantedExt/NumberTheory/NonSquarefreeBaseTwoPseudoprimeWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/NonSquarefreeBaseTwoPseudoprimeWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/fermat-pseudoprimes/index.html#conjecture).

## A non-squarefree base-two pseudoprime beyond $10^{13}$ exists

There is a natural number
$n > 10^{13}$ that is a Fermat pseudoprime to base $2$ (a composite number $n > 1$ with
$n \mid 2^{n-1} - 1$) and is not squarefree.

OEIS A158358 gives the witness $n = 10063351640161 = 73 \cdot 257 \cdot 449 \cdot 1093^2$.

## Sources

- OEIS A158358, nonsquarefree Poulet numbers, https://oeis.org/A158358.

Stated but not proved: `MathlibExt.NumberTheory.NonSquarefreeBaseTwoPseudoprimeWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/NonSquarefreeBaseTwoPseudoprimeWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/NonSquarefreeBaseTwoPseudoprimeWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/fermat-pseudoprimes/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fermat pseudoprimes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/fermat-pseudoprimes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/fermat-pseudoprimes)
