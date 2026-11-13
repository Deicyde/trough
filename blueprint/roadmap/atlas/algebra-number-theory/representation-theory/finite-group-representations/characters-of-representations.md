---
declaration: section
origin: cited
lean: CharacterTheory.char_inv_eq_conj, CharacterTheory.char_dual_eq_conj, CharacterTheory.classInnerProduct, CharacterTheory.irreducible_iff_classInnerProduct_self_eq_one, CharacterTheory.hasEigenvalue_pow_orderOf_eq_one, CharacterTheory.hasEigenvalue_pow_card_eq_one, CharacterTheory.char_charpoly_roots_pow_eq_one, CharacterTheory.character_selfPairing_eq_sum_sq
statement: formalized
proof: formalized
---

# Characters of representations

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/characters-of-representations/index.html).

## Character values at inverses are complex conjugates

Let $\rho$ be a representation of a
finite group $G$ on a finite-dimensional complex vector space $V$, with character $\chi_\rho$.
For every $g \in G$, $\chi_\rho(g^{-1}) = \overline{\chi_\rho(g)}$.

Formalized by `CharacterTheory.char_inv_eq_conj`, a theorem declared in [MathlibExt/RepresentationTheory/CharacterInvEqConj.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/CharacterInvEqConj.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/characters-of-representations/index.html#char-inv-eq-conj).

## Character of the dual representation

Let $\rho$ be a representation of a finite group
$G$ on a finite-dimensional complex vector space $V$, and let $\rho^*$ be its dual representation.
For every $g \in G$, the character of $\rho^*$ at $g$ is the complex conjugate of the character of
$\rho$ at $g$: $\chi_{\rho^*}(g) = \overline{\chi_\rho(g)}$.

Formalized by `CharacterTheory.char_dual_eq_conj`, a theorem declared in [MathlibExt/RepresentationTheory/CharacterInvEqConj.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/CharacterInvEqConj.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/characters-of-representations/index.html#char-dual-eq-conj).

## Class inner product

Let $G$ be a finite group and $k$ a field in which $|G|$ is
invertible. For functions $f_1, f_2 \colon G \to k$, their class inner product is
$\langle f_1, f_2 \rangle = |G|^{-1} \sum_{g \in G} f_1(g) f_2(g^{-1})$.

Formalized by `CharacterTheory.classInnerProduct`, a definition declared in [MathlibExt/RepresentationTheory/CharacterIrreducibleCriterion.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/CharacterIrreducibleCriterion.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/characters-of-representations/index.html#class-inner-product).

## Character criterion for irreducibility

A finite-dimensional
representation `σ` of a finite group over an algebraically closed field of
characteristic zero is irreducible if and only if the self-pairing of its
character is `1`.

Formalized by `CharacterTheory.irreducible_iff_classInnerProduct_self_eq_one`, a theorem declared in [MathlibExt/RepresentationTheory/CharacterIrreducibleCriterion.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/CharacterIrreducibleCriterion.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/characters-of-representations/index.html#irreducible-iff-class-inner-product-self).

## Eigenvalues of $\rho(g)$ are roots of unity of order dividing that of $g$

Let $\rho$ be a
representation of a finite group $G$ on a finite-dimensional complex vector space $V$, let
$g \in G$, and let $\operatorname{ord}(g)$ be the order of $g$. Every eigenvalue $\mu$ of $\rho(g)$
satisfies $\mu^{\operatorname{ord}(g)} = 1$.

The minimal polynomial of $\rho(g)$ divides $X^{\operatorname{ord}(g)} - 1$, and $\mu$ is a root of
the minimal polynomial.

Formalized by `CharacterTheory.hasEigenvalue_pow_orderOf_eq_one`, a theorem declared in [MathlibExt/RepresentationTheory/CharacterRootsOfUnity.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/CharacterRootsOfUnity.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/characters-of-representations/index.html#has-eigenvalue-pow-order-of-eq-one).

## Eigenvalues of $\rho(g)$ are $|G|$-th roots of unity

Let $\rho$ be a representation of a
finite group $G$ on a finite-dimensional complex vector space $V$, and let $g \in G$. Every
eigenvalue $\mu$ of $\rho(g)$ satisfies $\mu^{|G|} = 1$.

This follows because the order of $g$ divides $|G|$.

Formalized by `CharacterTheory.hasEigenvalue_pow_card_eq_one`, a theorem declared in [MathlibExt/RepresentationTheory/CharacterRootsOfUnity.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/CharacterRootsOfUnity.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/characters-of-representations/index.html#has-eigenvalue-pow-card-eq-one).

## Characteristic roots of $\rho(g)$ are $|G|$-th roots of unity

Let $\rho$ be a
representation of a finite group $G$ on a finite-dimensional complex vector space $V$, and let
$g \in G$. Every root $\mu$ of the characteristic polynomial of the matrix of $\rho(g)$ in a fixed
basis of $V$ satisfies $\mu^{|G|} = 1$.

Formalized by `CharacterTheory.char_charpoly_roots_pow_eq_one`, a theorem declared in [MathlibExt/RepresentationTheory/CharacterRootsOfUnity.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/CharacterRootsOfUnity.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/characters-of-representations/index.html#char-charpoly-roots-pow-eq-one).

## Parseval / sum-of-squares for characters

If `χ` is a combination
of the characters of pairwise non-equivalent irreducible representations
with coefficients `n i`, then the self-pairing of `χ` is the sum of the
squares of the coefficients. In particular, for a single irreducible
`ρ`, taking `χ = χ_ρ` gives self-pairing `1`, and for the regular
character the formula recovers `∑ (dim ρ_i) ^ 2 = |G|` once the regular
character is expanded in irreducibles.

Formalized by `CharacterTheory.character_selfPairing_eq_sum_sq`, a theorem declared in [MathlibExt/RepresentationTheory/CharacterSumOfSquares.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/CharacterSumOfSquares.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/characters-of-representations/index.html#character-self-pairing-eq-sum-sq).

## Sum of squares of the Wedderburn block sizes

If `|G|` is nonzero in
an algebraically closed field, the group algebra of a finite group is a product
of matrix algebras with nonzero block sizes whose squares sum to `|G|`.

Formalized by `CharacterTheory.wedderburn_sum_sq_eq_card`, a theorem declared in [MathlibExt/RepresentationTheory/CharacterSumOfSquares.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/CharacterSumOfSquares.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/characters-of-representations/index.html#wedderburn-sum-sq-eq-card).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Characters of representations](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/characters-of-representations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RepresentationTheory/finite-group-representations/characters-of-representations)
