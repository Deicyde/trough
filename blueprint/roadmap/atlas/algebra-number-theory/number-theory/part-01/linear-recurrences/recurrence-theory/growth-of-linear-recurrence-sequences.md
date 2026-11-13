---
declaration: section
origin: cited
lean: MetaMathlibExt.exists_norm_lt_pow_of_isSolution, MetaMathlibExt.c_recursive_exponential_growth_bound
statement: formalized
proof: formalized
---

# Growth of linear recurrence sequences

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/growth-of-linear-recurrence-sequences/index.html).

## Exponential growth bound for solutions of linear recurrences

Let $k$ be a natural
number, let $c_0, \dots, c_{k-1}$ be complex numbers, and let $t : \mathbb{N} \to \mathbb{C}$
satisfy $t(n+k) = \sum_{i=0}^{k-1} c_i \, t(n+i)$ for all $n \in \mathbb{N}$. Then there is an
integer $g \ge 1$ such that $|t(n)| < g^{n+1}$ for all $n \in \mathbb{N}$.

Formalized by `MetaMathlibExt.exists_norm_lt_pow_of_isSolution`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/CRecursiveExponentialGrowth.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/CRecursiveExponentialGrowth.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/growth-of-linear-recurrence-sequences/index.html#exists-norm-lt-pow-of-is-solution).

## Exponential growth bound for C-recursive sequences

Let $t : \mathbb{N} \to \mathbb{C}$ be
C-recursive: there are an order $k \ge 1$ and complex numbers $c_0, \dots, c_{k-1}$ with
$t(n+k) = \sum_{i=0}^{k-1} c_i \, t(n+i)$ for all $n \in \mathbb{N}$. Then there is an integer
$g \ge 1$ such that $|t(n)| < g^{n+1}$ for all $n \in \mathbb{N}$.

## Sources

- M. Prunescu and J. M. Shunia, "On Modular Representations of C-Recursive Integer Sequences," Journal of Integer Sequences 28 (2025), Article 25.5.3, Lemma (quoting Prunescu and Sauras-Altuzarra, Lemma 4), lines 166–167, https://cs.uwaterloo.ca/journals/JIS/VOL28/Prunescu/prunescu3.tex

Formalized by `MetaMathlibExt.c_recursive_exponential_growth_bound`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/CRecursiveExponentialGrowth.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/CRecursiveExponentialGrowth.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/growth-of-linear-recurrence-sequences/index.html#c-recursive-exponential-growth-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Growth of linear recurrence sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/growth-of-linear-recurrence-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/recurrence-theory/growth-of-linear-recurrence-sequences)
