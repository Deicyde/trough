---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.NormalFamilies.IsLocallyUniformlyBoundedOn, MathlibExt.Analysis.Complex.NormalFamilies.isLocallyUniformlyBoundedOn_of_forall_norm_le, MathlibExt.Analysis.Complex.NormalFamilies.IsLocallyUniformlyBoundedOn.exists_bound_of_isCompact, MathlibExt.Analysis.Complex.NormalFamilies.montel, MathlibExt.Analysis.Complex.NormalFamilies.vitali
statement: formalized
proof: formalized
---

# Normal families

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/normal-families/index.html).

## Locally uniformly bounded sequence of functions

Let $U \subseteq \mathbb{C}$ and let
$(F_n)_{n \in \mathbb{N}}$ be a sequence of functions $\mathbb{C} \to \mathbb{C}$. The sequence is
locally uniformly bounded on $U$ when every $x \in U$ has an open neighbourhood $V \subseteq U$
and a real $C \ge 0$ such that $|F_n(y)| \le C$ for all $n \in \mathbb{N}$ and all $y \in V$.

Formalized by `MathlibExt.Analysis.Complex.NormalFamilies.IsLocallyUniformlyBoundedOn`, a definition declared in [MathlibExt/Analysis/Complex/NormalFamilies.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/NormalFamilies.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/normal-families/index.html#is-locally-uniformly-bounded-on).

## A uniformly bounded sequence on an open set is locally uniformly bounded

Let
$U \subseteq \mathbb{C}$ be open, let $(F_n)_{n \in \mathbb{N}}$ be a sequence of functions
$\mathbb{C} \to \mathbb{C}$ and let $C \ge 0$ be real. If $|F_n(y)| \le C$ for all
$n \in \mathbb{N}$ and all $y \in U$, then $(F_n)$ is locally uniformly bounded on $U$.

Formalized by `MathlibExt.Analysis.Complex.NormalFamilies.isLocallyUniformlyBoundedOn_of_forall_norm_le`, a theorem declared in [MathlibExt/Analysis/Complex/NormalFamilies.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/NormalFamilies.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/normal-families/index.html#is-locally-uniformly-bounded-on-of-foral).

## Locally uniformly bounded sequences are uniformly bounded on compact subsets

Let
$(F_n)_{n \in \mathbb{N}}$ be a sequence of functions $\mathbb{C} \to \mathbb{C}$ that is locally
uniformly bounded on $U \subseteq \mathbb{C}$. Then for every compact set $K \subseteq U$ there is
a real $C \ge 0$ with $|F_n(y)| \le C$ for all $n \in \mathbb{N}$ and all $y \in K$.

Formalized by `MathlibExt.Analysis.Complex.NormalFamilies.IsLocallyUniformlyBoundedOn.exists_bound_of_isCompact`, a theorem declared in [MathlibExt/Analysis/Complex/NormalFamilies.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/NormalFamilies.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/normal-families/index.html#exists-bound-of-is-compact).

## Montel's theorem

Let $U \subseteq \mathbb{C}$ be open and let $(F_n)_{n \in \mathbb{N}}$ be a
sequence of functions $\mathbb{C} \to \mathbb{C}$, each holomorphic on $U$, that is locally
uniformly bounded on $U$. Then there are a strictly increasing map
$\varphi : \mathbb{N} \to \mathbb{N}$ and a function $f : \mathbb{C} \to \mathbb{C}$, holomorphic
on $U$, such that $F_{\varphi(n)} \to f$ locally uniformly on $U$ as $n \to \infty$.

## Sources

- Montel's theorem on normal families, P. Montel 1912/1927; see Ahlfors, Functions of One Complex Variable II; Lean is locally uniformly bounded holomorphic family with strictly monotone subsequence locally uniform convergent to holomorphic limit, open U form.

Formalized by `MathlibExt.Analysis.Complex.NormalFamilies.montel`, a theorem declared in [MathlibExt/Analysis/Complex/NormalFamilies.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/NormalFamilies.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/normal-families/index.html#montel).

## Vitali's convergence theorem

Let $U \subseteq \mathbb{C}$ be open and preconnected, and let
$(F_n)_{n \in \mathbb{N}}$ be a sequence of functions $\mathbb{C} \to \mathbb{C}$, each holomorphic
on $U$, that is locally uniformly bounded on $U$. Let $S \subseteq U$ have an accumulation point
$x_0 \in U$, and let $g : \mathbb{C} \to \mathbb{C}$ satisfy $F_n(z) \to g(z)$ as $n \to \infty$
for every $z \in S$. Then there is a function $f : \mathbb{C} \to \mathbb{C}$, holomorphic on $U$,
with $f(z) = g(z)$ for all $z \in S$, such that $F_n \to f$ locally uniformly on $U$.

## Sources

- Vitali convergence theorem, G. Vitali 1903; see Hille, Analytic Function Theory Vol II and Conway II; Lean is open preconnected U locally uniformly bounded with AccPt accumulation and pointwise limit on S extends to locally uniform holomorphic convergence, Montel-related strengthening.

Formalized by `MathlibExt.Analysis.Complex.NormalFamilies.vitali`, a theorem declared in [MathlibExt/Analysis/Complex/NormalFamilies.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/NormalFamilies.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/normal-families/index.html#vitali).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Normal families](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/normal-families/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/cauchy-theory/normal-families)
