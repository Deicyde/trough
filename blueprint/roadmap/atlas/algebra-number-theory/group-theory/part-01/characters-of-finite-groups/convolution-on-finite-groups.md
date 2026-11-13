---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FiniteGroupConvolutionWanted.conv, MathlibExt.GroupTheory.FiniteGroupConvolutionWanted.conv_assoc, MathlibExt.GroupTheory.FiniteGroupConvolutionWanted.conv_single_one, MathlibExt.GroupTheory.FiniteGroupConvolutionWanted.conv_comm_of_comm, MathlibExt.GroupTheory.FiniteGroupConvolutionWanted.charPair_conv
statement: formalized
proof: formalized
---

# Convolution on finite groups

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/convolution-on-finite-groups/index.html).

## Convolution on a finite group

For a finite group $G$ and functions
$f, g : G \to \mathbb{C}$, the convolution $f \ast g : G \to \mathbb{C}$ is defined by
$(f \ast g)(x) = \sum_{y \in G} f(y)\, g(y^{-1} x)$ for $x \in G$.

Formalized by `MathlibExt.GroupTheory.FiniteGroupConvolutionWanted.conv`, a definition declared in [MathlibExt/GroupTheory/FiniteGroupConvolution.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/FiniteGroupConvolution.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/convolution-on-finite-groups/index.html#conv).

## Associativity of convolution

Let $G$ be a finite group and write $f \ast g$ for the
convolution $(f \ast g)(x) = \sum_{y \in G} f(y)\, g(y^{-1} x)$ of functions on $G$. For all
$f, g, h : G \to \mathbb{C}$ we have $(f \ast g) \ast h = f \ast (g \ast h)$.

Proof: Expand into double sums, swap them, and reindex by left multiplication,
following the finite group-algebra argument in Terras, Ch. 1.

## Sources

- A. Terras, Fourier Analysis on Finite Groups and Applications, Ch. 1 (the group algebra).

Formalized by `MathlibExt.GroupTheory.FiniteGroupConvolutionWanted.conv_assoc`, a theorem declared in [MathlibExt/GroupTheory/FiniteGroupConvolution.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/FiniteGroupConvolution.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/convolution-on-finite-groups/index.html#conv-assoc).

## The delta function at the identity is a left unit for convolution

Let $G$ be a finite group,
write $f \ast g$ for the convolution $(f \ast g)(x) = \sum_{y \in G} f(y)\, g(y^{-1} x)$ of
functions on $G$, and let $\delta_1 : G \to \mathbb{C}$ be given by $\delta_1(1) = 1$ and
$\delta_1(x) = 0$ for $x \neq 1$. Then $\delta_1 \ast f = f$ for every $f : G \to \mathbb{C}$.

Proof: Expand the convolution and collapse the sum at the unique nonzero value
of the delta function, following the identity-element argument in Terras, Ch. 1.

## Sources

- A. Terras, Fourier Analysis on Finite Groups and Applications, Ch. 1 (identity of the group algebra).

Formalized by `MathlibExt.GroupTheory.FiniteGroupConvolutionWanted.conv_single_one`, a theorem declared in [MathlibExt/GroupTheory/FiniteGroupConvolution.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/FiniteGroupConvolution.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/convolution-on-finite-groups/index.html#conv-single-one).

## Convolution on a finite abelian group is commutative

Let $G$ be a finite abelian group and
write $f \ast g$ for the convolution $(f \ast g)(x) = \sum_{y \in G} f(y)\, g(y^{-1} x)$ of
functions on $G$. For all $f, g : G \to \mathbb{C}$ we have $f \ast g = g \ast f$.

Proof: Reindex by $y \mapsto y^{-1} x$ and use commutativity in $G$ and in $\mathbb{C}$,
as in the commutative group-algebra argument in Terras, Ch. 2.

## Sources

- A. Terras, Fourier Analysis on Finite Groups and Applications, Ch. 2 (commutative group algebra of an abelian group).

Formalized by `MathlibExt.GroupTheory.FiniteGroupConvolutionWanted.conv_comm_of_comm`, a theorem declared in [MathlibExt/GroupTheory/FiniteGroupConvolution.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/FiniteGroupConvolution.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/convolution-on-finite-groups/index.html#conv-comm-of-comm).

## Convolution theorem for one-dimensional characters

Let $G$ be a finite group, let
$\varphi : G \to \mathbb{C}$ satisfy $\varphi(1) = 1$ and $\varphi(xy) = \varphi(x)\varphi(y)$
for all $x, y \in G$ (a one-dimensional character), and let $f, g : G \to \mathbb{C}$. Writing
$f \ast g$ for the convolution $(f \ast g)(x) = \sum_{y \in G} f(y)\, g(y^{-1} x)$, we have

$$
\sum_{x \in G} \varphi(x)\,(f \ast g)(x) =
\Big(\sum_{x \in G} \varphi(x) f(x)\Big)\Big(\sum_{x \in G} \varphi(x) g(x)\Big).
$$

Proof: Swap the finite sums, reindex by $x = yz$, and use multiplicativity of $\varphi$ to
factor the character pairing, following Terras, Ch. 2–3.

## Sources

- A. Terras, Fourier Analysis on Finite Groups and Applications, Ch. 2–3 (the Fourier transform takes convolution to pointwise products).

Formalized by `MathlibExt.GroupTheory.FiniteGroupConvolutionWanted.charPair_conv`, a theorem declared in [MathlibExt/GroupTheory/FiniteGroupConvolution.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/FiniteGroupConvolution.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/convolution-on-finite-groups/index.html#char-pair-conv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Convolution on finite groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/convolution-on-finite-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/characters-of-finite-groups/convolution-on-finite-groups)
