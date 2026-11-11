---
declaration: section
origin: cited
lean: MetaMathlibExt.IsPRecursiveSequence, MetaMathlibExt.binet_closed_form_second_order, MetaMathlibExt.skolemMahlerLech
statement: formalized
proof: formalized
---

# General theory of recurrences: its own results

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/index.html).

C-finite, P-recursive and MC-finite sequences, Binet formulas, Skolem–Mahler–Lech, growth, generating functions and decomposable forms.

## P-recursive sequences

Let $r$ be a natural number, let $P_0, \dots, P_r$ be polynomials
with integer coefficients, and let $(u_n)_{n \ge 0}$ be a sequence of integers. The sequence $u$
is P-recursive of order $r$ with coefficient polynomials $P_0, \dots, P_r$ if for every $n \ge r$,

$$
P_0(n)\, u_n = \sum_{i=1}^{r} P_i(n)\, u_{n-i}.
$$

Formalized by `MetaMathlibExt.IsPRecursiveSequence`, a definition declared in [MathlibExt/NumberTheory/PRecursiveSequence.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PRecursiveSequence.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/index.html#is-precursive-sequence).

## Binet formula for second-order linear recurrences

Let $K$ be a field, let
$P, Q, \alpha, \beta \in K$ with $\alpha \ne \beta$, and suppose that $\alpha$ and $\beta$ are
both roots of $z^2 - Pz + Q$. If a sequence $u : \mathbb{N} \to K$ satisfies
$u_{n+2} = P u_{n+1} - Q u_n$ for all $n$, then for every natural number $n$,

$$u_n = \frac{(u_1 - \beta u_0)\alpha^n - (u_1 - \alpha u_0)\beta^n}{\alpha - \beta}.$$

## Sources

- Hongshen Chua, "A Study of Second-Order Linear Recurrence Sequences via Continuants," Journal of Integer Sequences 26 (2023), Article 23.8.8, Theorem [Binet's formula], lines 270–274, <https://cs.uwaterloo.ca/journals/JIS/VOL26/Chua2/chua13.tex>.

Formalized by `MetaMathlibExt.binet_closed_form_second_order`, a theorem declared in [MathlibExt/NumberTheory/BinetClosedForm.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/BinetClosedForm.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/index.html#binet-closed-form-second-order).

## Skolem–Mahler–Lech theorem

Let $K$ be a field of characteristic zero, let $k$ be a
natural number, let $c_0, \dots, c_{k-1} \in K$, and let $u_0, u_1, u_2, \dots$ be a sequence in
$K$ satisfying the linear recurrence $u_{n+k} = \sum_{i=0}^{k-1} c_i u_{n+i}$ for all $n \ge 0$
(for $k = 0$ the sum is empty and every $u_n$ is $0$). Then there are a finite set
$F \subseteq \mathbb{N}$ and finitely many pairs $(a_1, d_1), \dots, (a_m, d_m)$ of natural numbers
with every $d_j > 0$ such that the zero set of the sequence is

$$\{n \in \mathbb{N} : u_n = 0\} = F \cup \bigcup_{j=1}^{m} \{a_j + d_j t : t \in \mathbb{N}\}.$$

The proof follows Lech's $p$-adic method: the data embed in $\mathbb{Z}_p$ for a suitable prime $p$
(a Cassels-type embedding), on each residue class modulo the period of the companion matrix
modulo $p$ the sequence is given by a convergent $p$-adic power series, and Strassmann's theorem
bounds its zeros. C. Lech, A note on recurring series, Ark. Mat. 2 (1953), 417–421;
J. W. S. Cassels, An embedding theorem for fields, Bull. Austral. Math. Soc. 14 (1976), 193–198.

## Sources

- https://en.wikipedia.org/wiki/Skolem%E2%80%93Mahler%E2%80%93Lech_theorem (statement id `skolem-lech-s1`).

Formalized by `MetaMathlibExt.skolemMahlerLech`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/SkolemMahlerLech.lean, line 914](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/SkolemMahlerLech.lean#L914). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/index.html#skolem-mahler-lech).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: General theory of recurrences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/recurrence-theory)
