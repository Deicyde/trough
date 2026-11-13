---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.Digits.GrundmanNivenBoundWanted.grundman_consecutive_niven_bound, MathlibExt.NumberTheory.TuDengConjectureWanted.tuDengConjecture_holds
statement: formalized
---

# Digit properties of integers: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/index.html).

Digit sums and products, Niven, happy, Kaprekar, Keith numbers, comma sequences, decimal expansions of fractions (Midy, repetends).

## Grundman's bound on consecutive Niven numbers

Let $b \ge 2$ and $a \ge 1$ be integers.
Then for some $i$ with $0 \le i \le 2b$, the integer $a + i$ is not divisible by the sum of its
base-$b$ digits. Equivalently, the $2b + 1$ consecutive integers $a, a + 1, \dots, a + 2b$ are not
all $b$-Niven numbers, where a $b$-Niven number is a positive integer divisible by the sum of its
base-$b$ digits.

## Sources

- Michael Gohn, Joshua Harrington, Sophia Lebiere, Hani Samamah, Kyla Shappell, and Tony W. H. Wong, "Arithmetic Progressions of b-Prodigious Numbers," Journal of Integer Sequences 25 (2022), Article 22.8.7, line 149, <https://cs.uwaterloo.ca/journals/JIS/VOL25/Wong/wong42.tex>, citing as the original result Heidi Grundman, "Sequences of consecutive n-Niven numbers," Fibonacci Quarterly 32 (1994), 174–175.

Formalized by `MathlibExt.NumberTheory.Digits.GrundmanNivenBoundWanted.grundman_consecutive_niven_bound`, a theorem declared in [MathlibExt/NumberTheory/Digits/GrundmanNivenBound.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Digits/GrundmanNivenBound.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/index.html#grundman-consecutive-niven-bound).

## Tu–Deng conjecture

For every integer $k \ge 2$ and every nonzero residue $t$ modulo
$2^k - 1$, the number of pairs $(a, b)$ of residues modulo $2^k - 1$ with $a + b = t$ and
$w(a) + w(b) \le k - 1$ is at most $2^{k-1}$, where $w(a)$ is the binary digit sum of the
representative of $a$ in $\{0, 1, \dots, 2^k - 2\}$.

## Sources

- T. W. Cusick, Proof of the Tu-Deng Conjecture, arXiv:2608.14821 (2026), https://arxiv.org/abs/2608.14821.

Stated but not proved: `MathlibExt.NumberTheory.TuDengConjectureWanted.tuDengConjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/TuDengConjectureWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TuDengConjectureWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/index.html#tu-deng-conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Digit properties of integers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/digits-numeration/digit-properties)
