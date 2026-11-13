---
declaration: section
origin: cited
lean: TensorProduct.toIntegralClosure_bijective_of_etale, vandermondeProd_isUnit, Algebra.Smooth.toIntegralClosure_bijective, TensorProduct.toIntegralClosure_bijective_of_directLimit, TensorProduct.toIntegralClosure_bijective_of_directLimit_smooth
statement: formalized
proof: formalized
---

# 10.147 Integral closure and smooth base change

Section 10.147 of the Stacks Project, [Tag 03GC](https://stacks.math.columbia.edu/tag/03GC). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03GE, a lemma

[Tag 03GE](https://stacks.math.columbia.edu/tag/03GE) in the Stacks Project.

**`TensorProduct.toIntegralClosure_bijective_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/IntegralClosure.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/IntegralClosure.lean#L59). The attribute's comment: “The isomorphism of the tag is bijectivity of Mathlib's canonical map `TensorProduct.toIntegralClosure`. The proof follows the tag: injectivity by flatness, then bijectivity is checked on principal opens of `Spec S` on which `S` is standard étale (00UE, Mathlib's `Algebra.IsEtaleAt.exists_isStandardEtale`), using that integral closure commutes with localization (0307) and the local criterion 00EO (Mathlib's `TensorProduct.toIntegralClosure_bijective_of_isLocalizationAway`); the standard étale case is Mathlib's `mem_adjoin_map_integralClosure_of_isStandardEtale`.”.

> Let `R → S` be an étale ring map, let `R → B` be any ring map, let
> `A = integralClosure R B` be the integral closure of `R` in `B` and let
> `A' = integralClosure S (S ⊗[R] B)` be the integral closure of `S` in `S ⊗[R] B`. Then the
> canonical map `S ⊗[R] A → A'`, `s ⊗ a ↦ s ⊗ a`, is an isomorphism.

```lean
theorem toIntegralClosure_bijective_of_etale [Algebra.Etale R S] :
    Function.Bijective (toIntegralClosure R S B)
```

## Tag 03GF, an example

[Tag 03GF](https://stacks.math.columbia.edu/tag/03GF) in the Stacks Project.

**`vandermondeProd_isUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RootsOfUnity/VandermondeUnit.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/RootsOfUnity/VandermondeUnit.lean#L250).

> **Stacks 03GF.** For every `d < p`, the element `Δ\_d = ∏\_\{0 ≤ i < j < d}
> (α\_i - α\_j)` is a unit in `R' = Z[1/p][x]/(Phi(x))`.
>
> Δ\_d is a double product of the differences `αᵢ - αⱼ`; each such difference (for
> `i < j < d ≤ p-1`) is a unit by `alpha_sub_isUnit`, and a product of units is a
> unit (`Finset.prod_induction` with `IsUnit.mul`, `isUnit_one`).

```lean
theorem vandermondeProd_isUnit (d : ℕ) (hd : d < p) : IsUnit (vandermondeProd p d)
```

## Tag 03GG, a lemma

[Tag 03GG](https://stacks.math.columbia.edu/tag/03GG) in the Stacks Project.

**`Algebra.Smooth.toIntegralClosure_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/BaseChange.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegralClosure/BaseChange.lean#L118). The attribute's comment: “The isomorphism of the tag is bijectivity of Mathlib's canonical map `TensorProduct.toIntegralClosure`, whose `AlgEquiv` form is `AlgEquiv.ofBijective` applied to it. This is Mathlib's `TensorProduct.toIntegralClosure_bijective_of_smooth`, which carries no `@[stacks]` tag upstream. See the module docstring.”. References: EGA IV (18.12.15), “more general”; EGA IV (6.14.5), “smooth base change”.

> Let `R → S` be a smooth ring map, let `R → B` be any ring map, let
> `A = integralClosure R B` be the integral closure of `R` in `B` and let
> `A' = integralClosure S (S ⊗[R] B)` be the integral closure of `S` in `S ⊗[R] B`. Then the
> canonical map `S ⊗[R] A → A'`, `s ⊗ a ↦ s ⊗ a`, is an isomorphism.

```lean
public theorem toIntegralClosure_bijective {R S B : Type*} [CommRing R] [CommRing S] [CommRing B]
    [Algebra R S] [Algebra R B] [Algebra.Smooth R S] :
    Function.Bijective (TensorProduct.toIntegralClosure R S B)
```

## Tag 0CBF, a lemma

[Tag 0CBF](https://stacks.math.columbia.edu/tag/0CBF) in the Stacks Project.

**`TensorProduct.toIntegralClosure_bijective_of_directLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/BaseChange.lean, line 371](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegralClosure/BaseChange.lean#L371). The attribute's comment: “The colimit step of the tag, with the smoothness of the stages weakened to what the argument uses: bijectivity of the map at each stage. The tag's own hypothesis is recovered in `TensorProduct.toIntegralClosure_bijective_of_directLimit_smooth` below. The filtered colimit is spelled as a colimit over a directed nonempty preorder, presented by an `R`-algebra equivalence `DirectLimit G F ≃ₐ[R] S` so that the conclusion is about an abstract `S`; the isomorphism of the tag is bijectivity of Mathlib's canonical map `TensorProduct.toIntegralClosure`, as in the smooth case 03GG. See the module docstring.”.

> Let `R → S` and `R → B` be ring maps, let `A = integralClosure R B` and let
> `A' = integralClosure S (S ⊗[R] B)`. If `S` is `R`-algebra isomorphic to the colimit
> `DirectLimit G F` of a directed system `G` of `R`-algebras and the canonical map
> `G i ⊗[R] A → integralClosure (G i) (G i ⊗[R] B)` is bijective for every `i`, then the canonical
> map `S ⊗[R] A → A'` is bijective.

```lean
public theorem TensorProduct.toIntegralClosure_bijective_of_directLimit
    {R S B : Type*} [CommRing R] [CommRing S] [CommRing B] [Algebra R S] [Algebra R B]
    {ι : Type*} [Preorder ι] [IsDirectedOrder ι] [Nonempty ι]
    {G : ι → Type*} [∀ i, CommRing (G i)] [∀ i, Algebra R (G i)]
    (F : ∀ i j, i ≤ j → (G i →ₐ[R] G j)) [DirectedSystem G fun i j h ↦ F i j h]
    (e : DirectLimit G F ≃ₐ[R] S)
    (H : ∀ i, Function.Bijective (TensorProduct.toIntegralClosure R (G i) B)) :
    Function.Bijective (TensorProduct.toIntegralClosure R S B)
```

**`TensorProduct.toIntegralClosure_bijective_of_directLimit_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/BaseChange.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegralClosure/BaseChange.lean#L390). The attribute's comment: “The literal form of the tag, as the colimit step `TensorProduct.toIntegralClosure_bijective_of_directLimit` applied to the smooth case 03GG (`TensorProduct.toIntegralClosure_bijective_of_smooth`).”. References: EGA IV (6.14.5), “colimit of smooth base”; EGA IV (18.12.15).

> Let `R → S` and `R → B` be ring maps, let `A = integralClosure R B` and let
> `A' = integralClosure S (S ⊗[R] B)`. If `S` is `R`-algebra isomorphic to the colimit
> `DirectLimit G F` of a directed system `G` of smooth `R`-algebras, then the canonical map
> `S ⊗[R] A → A'` is an isomorphism.

```lean
public theorem TensorProduct.toIntegralClosure_bijective_of_directLimit_smooth
    {R S B : Type*} [CommRing R] [CommRing S] [CommRing B] [Algebra R S] [Algebra R B]
    {ι : Type*} [Preorder ι] [IsDirectedOrder ι] [Nonempty ι]
    {G : ι → Type*} [∀ i, CommRing (G i)] [∀ i, Algebra R (G i)] [∀ i, Algebra.Smooth R (G i)]
    (F : ∀ i j, i ≤ j → (G i →ₐ[R] G j)) [DirectedSystem G fun i j h ↦ F i j h]
    (e : DirectLimit G F ≃ₐ[R] S) :
    Function.Bijective (TensorProduct.toIntegralClosure R S B)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.147, Tag 03GC](https://stacks.math.columbia.edu/tag/03GC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
