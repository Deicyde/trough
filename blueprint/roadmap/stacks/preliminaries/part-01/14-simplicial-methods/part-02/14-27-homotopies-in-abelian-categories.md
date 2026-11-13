---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialObject.HtpyRel.toChainHomotopy_hom_eq, CategoryTheory.SimplicialObject.IsHomotopy.toChainHomotopy_hom_eq, AlgebraicTopology.homotopic_normalizedMooreComplex_map, AlgebraicTopology.homotopyEquivalences_alternatingFaceMapComplex_map, AlgebraicTopology.homotopyEquivalences_normalizedMooreComplex_map
statement: formalized
proof: formalized
---

# 14.27 Homotopies in abelian categories

Section 14.27 of the Stacks Project, [Tag 019Q](https://stacks.math.columbia.edu/tag/019Q). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 019R, an equation

[Tag 019R](https://stacks.math.columbia.edu/tag/019R) in the Stacks Project.

**`CategoryTheory.SimplicialObject.HtpyRel.toChainHomotopy_hom_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/ChainHomotopy.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/ChainHomotopy.lean#L159). The attribute's comment: “the chain homotopy `s(h)` is `toChainHomotopy` of the bridge `HtpyRel.toHomotopy` to Mathlib's `SimplicialObject.Homotopy`, a chain homotopy between `s(a)` and `s(b)` (019S); stated is its degree-`n` component, in the source's form, for the family `h_{n,i}` of 019L; the components in the other bidegrees are zero by Mathlib's `Homotopy.ToChainHomotopy.hom_eq_zero`”.

> **The chain homotopy induced by a simplicial homotopy.** Let `h_{n,i} : Uₙ ⟶ Vₙ` be a family
> satisfying the relations of [Stacks, Tag 019L] relative to `a, b : U ⟶ V`, that is, a homotopy
> from `a` to `b` in the form of [Stacks, Tag 019M]. Then the degree-`n` component
> `s(h)ₙ : Uₙ ⟶ V_{n+1}` of the induced chain homotopy between `s(a)` and `s(b)` is
> `∑_{i=0}^{n} (-1)^{i+1} h_{n+1,i+1} ∘ sⁿᵢ`.

```lean
theorem toChainHomotopy_hom_eq (hrel : HtpyRel a b hc) (n : ℕ) :
    hrel.toHomotopy.toChainHomotopy.hom n (n + 1) =
      ∑ i : Fin (n + 1), ((-1 : ℤ) ^ ((i : ℕ) + 1)) • (U.σ i ≫ hc (n + 1) i.succ.castSucc)
```

**`CategoryTheory.SimplicialObject.IsHomotopy.toChainHomotopy_hom_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/ChainHomotopy.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/ChainHomotopy.lean#L184). The attribute's comment: “the homotopy is the morphism `h : U × Δ[1] ⟶ V` of 019K, as in the source's section 019Q, and `h_{n,i}` is `homotopyComponent h n i`; the chain homotopy `s(h)` is `toChainHomotopy` of the Mathlib homotopy `(htpy_forward a b h hh).toHomotopy` built from these components through 019L”.

> **The chain homotopy induced by a homotopy `U × Δ[1] ⟶ V`.** Let `h : U × Δ[1] ⟶ V` be a
> homotopy from `a` to `b` in the sense of [Stacks, Tag 019K], with components
> `h_{n,i} = homotopyComponent h n i : Uₙ ⟶ Vₙ`. Then the degree-`n` component
> `s(h)ₙ : Uₙ ⟶ V_{n+1}` of the induced chain homotopy between `s(a)` and `s(b)` is
> `∑_{i=0}^{n} (-1)^{i+1} h_{n+1,i+1} ∘ sⁿᵢ`.

```lean
theorem toChainHomotopy_hom_eq {h : U.copower Δ[1] ⟶ V} (hh : IsHomotopy h a b) (n : ℕ) :
    (htpy_forward a b h hh).toHomotopy.toChainHomotopy.hom n (n + 1) =
      ∑ i : Fin (n + 1),
        ((-1 : ℤ) ^ ((i : ℕ) + 1)) • (U.σ i ≫ homotopyComponent h (n + 1) i.succ.castSucc)
```

## Tag 019S, a lemma

[Tag 019S](https://stacks.math.columbia.edu/tag/019S) in the Stacks Project.

**`AlgebraicTopology.homotopic_normalizedMooreComplex_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/ChainHomotopy.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/ChainHomotopy.lean#L327). The attribute's comment: “the half about the Moore complex `s` is Mathlib's, so it gets no public name here: a homotopy gives `SimplicialObject.Homotopy.toChainHomotopy`, and `homotopy_congruence` propagates it along the source's chain; stated here is the half about `N`. `homotopic` is Mathlib's chain homotopy relation, and being homotopic is spelled `Relation.EqvGen fun a b => Nonempty (Homotopy a b)` as in 019W”. References: SGA 4½ Fonctions L (1.4), “N preserves homotopy”.

> **Homotopic morphisms have chain homotopic normalized Moore complexes.** If
> `a, b : U ⟶ V` are homotopic morphisms of simplicial objects of an abelian category `A` —
> related by a chain of morphisms consecutive members of which admit a simplicial homotopy in
> one direction or the other — then the induced maps `N(a), N(b) : N(U) ⟶ N(V)` of normalized
> Moore complexes are chain homotopic.

```lean
public theorem homotopic_normalizedMooreComplex_map
    (h : Relation.EqvGen (fun a b : U ⟶ V => Nonempty (Homotopy a b)) a b) :
    homotopic A (ComplexShape.down ℕ)
      ((normalizedMooreComplex A).map a) ((normalizedMooreComplex A).map b)
```

## Tag 019T, a lemma

[Tag 019T](https://stacks.math.columbia.edu/tag/019T) in the Stacks Project.

**`AlgebraicTopology.homotopyEquivalences_alternatingFaceMapComplex_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/ChainHomotopy.lean, line 349](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/ChainHomotopy.lean#L349). The attribute's comment: “the first sentence, for the Moore complex `s`, with the source's `additive` weakened to `Preadditive`, Mathlib's hypothesis for `alternatingFaceMapComplex`; the second sentence is `homotopyEquivalences_normalizedMooreComplex_map` below. Being a homotopy equivalence of chain complexes is `HomologicalComplex.homotopyEquivalences`, which pins the map, and the hypothesis is 019N's `SimplicialObject.homotopyEquivalences`”.

> **The Moore complex of a homotopy equivalence of simplicial objects is a homotopy
> equivalence of chain complexes.** Let `a : U ⟶ V` be a homotopy equivalence of simplicial
> objects of a preadditive category `A`: there is `b : V ⟶ U` with `a ≫ b` homotopic to `𝟙 U`
> and `b ≫ a` homotopic to `𝟙 V`, homotopic meaning related by the equivalence relation
> generated by the existence of a simplicial homotopy ([Stacks, Tag 019N]). Then
> `s(a) : s(U) ⟶ s(V)` is a homotopy equivalence of chain complexes.

```lean
public theorem homotopyEquivalences_alternatingFaceMapComplex_map [Preadditive A]
    (ha : SimplicialObject.homotopyEquivalences A a) :
    HomologicalComplex.homotopyEquivalences A (ComplexShape.down ℕ)
      ((alternatingFaceMapComplex A).map a)
```

**`AlgebraicTopology.homotopyEquivalences_normalizedMooreComplex_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/ChainHomotopy.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/ChainHomotopy.lean#L370). The attribute's comment: “the second sentence, for the normalized Moore complex `N`; the first is `homotopyEquivalences_alternatingFaceMapComplex_map` above, from which this one is deduced by conjugating with the natural homotopy equivalence `inclusionOfMooreComplexMap`. Only `Abelian A` is assumed, which provides the preadditivity the source's `additive` asks for. Being a homotopy equivalence of chain complexes is `HomologicalComplex.homotopyEquivalences`, which pins the map, and the hypothesis is 019N's `SimplicialObject.homotopyEquivalences`”.

> **The normalized Moore complex of a homotopy equivalence of simplicial objects is a
> homotopy equivalence of chain complexes.** Let `a : U ⟶ V` be a homotopy equivalence of
> simplicial objects of an abelian category `A` ([Stacks, Tag 019N]). Then
> `N(a) : N(U) ⟶ N(V)` is a homotopy equivalence of chain complexes.

```lean
public theorem homotopyEquivalences_normalizedMooreComplex_map [Abelian A]
    (ha : SimplicialObject.homotopyEquivalences A a) :
    HomologicalComplex.homotopyEquivalences A (ComplexShape.down ℕ)
      ((normalizedMooreComplex A).map a)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.27, Tag 019Q](https://stacks.math.columbia.edu/tag/019Q)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
