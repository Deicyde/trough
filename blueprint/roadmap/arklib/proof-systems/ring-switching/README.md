# Ring Switching

*Ring switching* is a reduction that turns a multilinear evaluation claim over a *small* coefficient ring $B$ into an evaluation claim over a *large* extension $L$, paying only an additive $O(1/\lvert L\rvert)$ soundness cost and *without re-committing* over $L$. It is the technique that lets a polynomial commitment scheme commit cheaply over a tiny ring (a binary-tower field, $\mathbb{F}_2$, or a cyclotomic ring $R_q$) while running sum-check and the final opening over a field large enough for soundness. It was introduced for binary towers in ([Diamond and Posen 2024](https://eprint.iacr.org/archive/2024/504/20250922:164810)). Hachi's extension-field-to-cyclotomic-ring reduction ([Nguyen et al. 2026](https://eprint.iacr.org/2026/156)) uses a related trace-based head.

ArkLib defines the DP24 prefix instance through a shared checked head and product sum-check. Its *packing profile* specifies the tensor carrier and coordinates; the binary-tower (Binius) construction supplies one instance. The coordinate layer also supports Hachi's separate trace head and reference-Flock packing algebra. New scalar consumers instantiate the shared protocol, while the interaction-layer Flock source, residual-relation and extraction transport remain separate obligations.

## The packing profile

The data and algebraic laws of the DP24 tensor presentation are collected into a single structure.

- [Ring-switching profile](def-ring-switching-profile.md)

The column inverse

$$
\mathrm{decomposeColumns}\Bigl(\sum_v \varphi_0(c_v)\varphi_1(\beta_v)\Bigr) = c
$$

is derived from the row inverse and the reconstruction laws.

Laws [(1)](def-ring-switching-profile.md)–[(2)](def-ring-switching-profile.md) fix the coordinate convention of ([Diamond and Posen 2024](https://eprint.iacr.org/archive/2024/504/20250922:164810), §2.5). They are data-layer reconstruction laws, not completeness or soundness statements. Protocol correctness additionally needs identities connecting these coordinates to packing, the honest folded element, and the batched multiplier. Together with the inverse laws, each coordinate map is a bijection $A \cong (\{0,1\}^\kappa \to L)$ (`rowEquiv`, `columnEquiv`); additivity, compatibility of rows with multiplication by $\varphi_1$ and of columns with multiplication by $\varphi_0$, and the coordinates of pure tensors $\varphi_0(x)\varphi_1(y)$ follow from the laws. The laws do not by themselves establish a valid protocol instance or a security theorem.

- [Tensor-product profile](def-tensor-product-profile.md)

A trace or automorphism switch whose carrier is $L$ itself, such as Hachi's §3 head ([Nguyen et al. 2026](https://eprint.iacr.org/2026/156)) with $A = R_q$, is not an instance when $\kappa > 0$: for a finite nontrivial $L$ the inverse laws force $\lvert A\rvert = \lvert L\rvert^{2^\kappa}$. Hachi's head uses the finite-coordinate packing layer directly instead: its packing data has the fixed subring as opening algebra, with one opening coordinate and $\psi$ as packing basis, its scalar source is a claim layout over the monomial coefficients of the packed variables, and its packed polynomial is the shared packed multilinear of the layout's components. Its conformance theorem states the head's accepting condition through that layer: the sent ring value is the single slice of the shared packed multilinear at the retained point, and the claimed scalar is the layout-weighted sum of its $\psi$-coordinates. The head's read-back is a checked observation (the $\psi$-coordinate inner product, equivalent to the trace check). Hachi §3.1 exercises only the packing, evaluation and opening part of the shared layer (one opening coordinate, no batching, multiplier or sumcheck), as in the paper, so its reuse is small at the proof level and real at the statement level. Because $R_q$ is not an integral domain its soundness is a separate argument (coordinate-wise special soundness into the ring-level evaluation relation).

## Packing the witness

- [Multilinear packing](def-pack-mle.md)

## The reduction

The shared protocol composes a checked head with product sum-check. Its endpoint is an evaluation of the same committed packed polynomial, retaining the original query and batching challenge. An opening must accept that contextual evaluation relation to close the protocol. The DP24 instance uses packing, opening and challenge algebras all equal to $L$, with prefix packing in the profile basis; its first message keeps the original carrier $A$.

- [Stages of the ring-switching reduction](def-ring-switching-stages.md)

For the concrete Binius construction, specialize the base to a finite field $K$ of cardinality $2$ and let $L$ be a finite extension field with a $K$-basis $\beta$ indexed by $\{0,\ldots,2^\kappa-1\}$, normalized by $\beta_0=1$. Use its associated tensor-product profile. Choose $\ell=\ell'+\kappa$, positive integers $\ell'$, $R$ and $\vartheta$ with $\vartheta\mid\ell'$ and $\ell'+R<2^\kappa$, and a number of opening queries $\gamma\in\mathbb{N}$. Challenges in $L$ use the uniform sampler.

- [Full Binius ring-switching reduction](def-full-ring-switching.md)

## Security

Oracle compatibility specifies the relations certified about the program. Honest coverage is separate: a `PackedCommitment.Honest` supplies a compatible oracle statement for every packed polynomial. It is not a security premise. The following completeness result applies to valid inputs with exact encodings; it does not assert completeness for every oracle within a decoding radius.

- [Perfect completeness](thm-ring-switching-completeness.md)
- [Round-by-round knowledge soundness of the prefix protocol](thm-ring-switching-core-soundness.md)
- [Closing a contextual opening](thm-ring-switching-soundness.md)
- [Binius with Binary Basefold](thm-binius-ring-switching-soundness.md)

Every checking verifier aborts on a failed check, so each verifier above has a guarded form and the round-by-round guarantees imply ordinary knowledge soundness at the summed error.

- [Knowledge soundness](thm-ring-switching-knowledge-soundness.md)
