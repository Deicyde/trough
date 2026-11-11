---
declaration: section
origin: cited
lean: MetaMathlibExt.acceptableNumbering_fixed_point, MetaMathlibExt.rice_theorem
statement: formalized
proof: formalized
---

# Rice's theorem for acceptable numberings

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/rice-s-theorem-for-acceptable-numberings/index.html).

## Rogers's fixed-point theorem for acceptable numberings

Let $\varphi$ assign to each
natural number $e$ a partial function $\varphi_e : \mathbb{N} \rightharpoonup \mathbb{N}$, and
suppose that the universal function $(e, n) \mapsto \varphi_e(n)$ is partial computable, that
every partial computable function $f : \mathbb{N} \rightharpoonup \mathbb{N}$ equals $\varphi_e$
for some $e$, and that for every partial computable
$g : \mathbb{N} \times \mathbb{N} \rightharpoonup \mathbb{N}$ there is a total computable
$s : \mathbb{N} \to \mathbb{N}$ with $\varphi_{s(e)}(n) = g(e, n)$ for all $e$ and $n$. Then for
every total computable $h : \mathbb{N} \to \mathbb{N}$ there is an $e$ with
$\varphi_e(n) = \varphi_{h(e)}(n)$ for all $n$.

Formalized by `MetaMathlibExt.acceptableNumbering_fixed_point`, a theorem declared in [MathlibExt/Computability/RiceTheorem.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Computability/RiceTheorem.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/rice-s-theorem-for-acceptable-numberings/index.html#acceptable-numbering-fixed-point).

## Rice's theorem for acceptable numberings

Let $\varphi$ assign to each natural number $e$
a partial function $\varphi_e : \mathbb{N} \rightharpoonup \mathbb{N}$, and suppose that every
$\varphi_e$ is partial computable, that the universal function $(e, n) \mapsto \varphi_e(n)$ is
partial computable, that every partial computable function
$f : \mathbb{N} \rightharpoonup \mathbb{N}$ equals $\varphi_e$ for some $e$, and that for every
partial computable $g : \mathbb{N} \times \mathbb{N} \rightharpoonup \mathbb{N}$ there is a total
computable $s : \mathbb{N} \to \mathbb{N}$ with $\varphi_{s(e)}(n) = g(e, n)$ for all $e$ and $n$.
Let $C \subseteq \mathbb{N}$ be a set of indices closed under extensional equality, that is, if
$\varphi_a(n) = \varphi_b(n)$ for all $n$, then $a \in C$ if and only if $b \in C$; and suppose
that $C$ is neither empty nor all of $\mathbb{N}$. Then there is no total computable
$d : \mathbb{N} \to \mathbb{N}$ such that, for every $e$, $e \in C$ if and only if $d(e) = 1$,
and $e \notin C$ if and only if $d(e) = 0$.

Proof: The standard argument first derives Kleene's recursion theorem for the acceptable
numbering, then diagonalizes a putative decider, following Rice (1953), Rogers §11.2, and
Soare II.3.1.

## Sources

- H. G. Rice, *Classes of recursively enumerable sets and their decision problems*, Transactions of the American Mathematical Society 74(2) (1953), 358-366.

Formalized by `MetaMathlibExt.rice_theorem`, a theorem declared in [MathlibExt/Computability/RiceTheorem.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Computability/RiceTheorem.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/rice-s-theorem-for-acceptable-numberings/index.html#rice-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rice's theorem for acceptable numberings](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/rice-s-theorem-for-acceptable-numberings/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/computability/rice-s-theorem-for-acceptable-numberings)
