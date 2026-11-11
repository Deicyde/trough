---
declaration: section
origin: cited
lean: CategoryTheory.Sheaf.createsLimitsOfShape, CategoryTheory.Sheaf.terminal, CategoryTheory.Sheaf.isTerminalTerminal, CategoryTheory.GrothendieckTopology.plusObj, CategoryTheory.GrothendieckTopology.toPlus, CategoryTheory.GrothendieckTopology.toPlus_naturality, CategoryTheory.GrothendieckTopology.intersection_covering, CategoryTheory.PreZeroHypercover.H0.mapOver_eq_of_homOver
statement: formalized
proof: formalized
---

# 7.10 Sheafification

Section 7.10 of the Stacks Project, [Tag 00W1](https://stacks.math.columbia.edu/tag/00W1). 17 tags here are carried by 14 declarations of the repository (all in StacksFrontier) and 18 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00W2, a lemma

[Tag 00W2](https://stacks.math.columbia.edu/tag/00W2) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Sheaf.createsLimitsOfShape`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.createsLimitsOfShape#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Sheafification/PlusFunctorial.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Sheafification/PlusFunctorial.lean#L21) (StacksCore): “the inclusion of sheaves into presheaves creates limits of any shape, so limits of diagrams of sheaves of sets exist and agree with the limits computed in presheaves”. References: EGA 0 (3.2.6), “more general”; SGA 3 IV (4.4.1), “more general”; SGA 4 II (4.1), “more general”.

## Tag 00W3, an example

[Tag 00W3](https://stacks.math.columbia.edu/tag/00W3) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Sheaf.terminal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.terminal#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Sheaf.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Sheaf.lean#L23) (StacksCore): “the singleton sheaf: the constant sheaf on a terminal object of the value category, which for sheaves of sets is the presheaf with a single section over every object”. References: SGA 3 I (1.2).
- [`CategoryTheory.Sheaf.isTerminalTerminal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.isTerminalTerminal#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Sheaf.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Sheaf.lean#L26) (StacksCore): “the singleton sheaf is a terminal object of the category of sheaves, i.e. the limit of the empty diagram of sheaves”. References: SGA 3 I (1.2), “special case”; SGA 3 I (2.1.1), “partial”; SGA 4 VI (7.4.13.5), “special case”.

## Tag 00W4, a lemma

[Tag 00W4](https://stacks.math.columbia.edu/tag/00W4) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.GrothendieckTopology.plusObj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.plusObj#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Plus.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Plus.lean#L44) (StacksCore): “The presheaf `F⁺`. Mathlib builds the colimit over covering sieves rather than over covering families, i.e. the functor `L` of Stacks section 7.49; the functoriality in the object that 00W4 asserts is the `map` field of this functor, and its compatibility with composition `F⁺(U) → F⁺(V) → F⁺(W)` is `Functor.map_comp`, which is exactly what the proof of 00W4 verifies.”. References: SGA 3 IV (4.3.10.0), “more general”; SGA 4 II (3.0.5); SGA 4 II (3.2); SGA 4 V (2.4.5), “special case”.
- [`CategoryTheory.GrothendieckTopology.toPlus`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.toPlus#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Plus.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Plus.lean#L51) (StacksCore): “The canonical map of presheaves `F → F⁺` of 00W4.”. References: SGA 3 IV (4.3.10.0), “more general”; SGA 4 II (3.0.5); SGA 4 II (3.2).

## Tag 00W5, a lemma

[Tag 00W5](https://stacks.math.columbia.edu/tag/00W5) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.GrothendieckTopology.toPlus_naturality`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.toPlus_naturality#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Sheafification/PlusSeparated.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Sheafification/PlusSeparated.lean#L20) (StacksCore): “the plus construction is functorial: the canonical maps `F ⟶ F⁺` are natural in `F`”.

## Tag 00W6, a lemma

[Tag 00W6](https://stacks.math.columbia.edu/tag/00W6) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.GrothendieckTopology.intersection_covering`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.intersection_covering#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Sheafification/PlusMonoOnSeparated.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheafification/PlusMonoOnSeparated.lean#L22) (StacksFrontier): “common refinement”. References: SGA 3 IV (4.2.1), “T′5 with F representable”; SGA 4 II (1.1.1), “finite intersections”.

## Tag 00W7, a lemma

[Tag 00W7](https://stacks.math.columbia.edu/tag/00W7) in the Stacks Project.

**`CategoryTheory.PreZeroHypercover.H0.mapOver_eq_of_homOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/CechH0.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheafification/CechH0.lean#L153).

> **Stacks 00W7.** Any two morphisms of families `𝒰 → 𝒱` inducing the same morphism of
> targets induce the same map `H⁰(𝒱, F) → H⁰(𝒰, F)`.
>
> Because `HomOver` carries the base morphism as a parameter, "inducing the same morphism of
> targets" is expressed by the two morphisms having the same type, and the statement is that the
> induced map depends on `g` alone. The proof applies the matching property of `s` at the single
> cone `(U_i, φ.h₀ i, ψ.h₀ i)`, which commutes over `V` precisely because both morphisms lie
> over `g`.

```lean
theorem H0.mapOver_eq_of_homOver {E : PreZeroHypercover.{w} U} {G : PreZeroHypercover.{w'} V}
    {g : U ⟶ V} (φ ψ : E.HomOver G g) : H0.mapOver F φ = H0.mapOver F ψ
```

## Tag 00W8, a remark

[Tag 00W8](https://stacks.math.columbia.edu/tag/00W8) in the Stacks Project.

**`CategoryTheory.PreZeroHypercover.H0.mapOver_bijective_of_mutual_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/CechH0.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheafification/CechH0.lean#L173).

> **Stacks 00W8.** If `𝒰` refines `𝒱` and `𝒱` refines `𝒰`, the two induced pullback maps on
> `H⁰` are mutually inverse bijections, so there is a canonical identification
> `H⁰(𝒰, F) = H⁰(𝒱, F)`.

```lean
theorem H0.mapOver_bijective_of_mutual_refinement {E G : PreZeroHypercover.{w} U}
    (φ : E.HomOver G (𝟙 U)) (ψ : G.HomOver E (𝟙 U)) :
    (∀ s : H0 F E, H0.mapOver F φ (H0.mapOver F ψ s) = s) ∧
      (∀ t : H0 F G, H0.mapOver F ψ (H0.mapOver F φ t) = t)
```

**`CategoryTheory.PreZeroHypercover.H0.refinementEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/CechH0.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheafification/CechH0.lean#L182).

> **Stacks 00W8**, packaged as the bijection `H⁰(𝒱, F) ≃ H⁰(𝒰, F)` determined by mutual
> refinements. By 00W7 it does not depend on which refinements are chosen.

```lean
def H0.refinementEquiv {E G : PreZeroHypercover.{w} U}
    (φ : E.HomOver G (𝟙 U)) (ψ : G.HomOver E (𝟙 U)) : H0 F G ≃ H0 F E
```

**`CategoryTheory.PreZeroHypercover.H0.refinementEquiv_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/CechH0.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheafification/CechH0.lean#L192). References: SGA 3 IV (1.12), “Clause, special case”.

> **Stacks 00W8**, the independence clause: the identification above is canonical, since any
> two refinements `𝒰 → 𝒱` induce the same map. This is 00W7 at `g = 𝟙 U`.

```lean
theorem H0.refinementEquiv_eq {E G : PreZeroHypercover.{w} U}
    (φ φ' : E.HomOver G (𝟙 U)) (ψ ψ' : G.HomOver E (𝟙 U)) :
    H0.refinementEquiv F φ ψ = H0.refinementEquiv F φ' ψ'
```

## Tag 00W9, a lemma

[Tag 00W9](https://stacks.math.columbia.edu/tag/00W9) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Presheaf.isLocallySurjective_toPlus`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Presheaf.isLocallySurjective_toPlus#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Sheafification/PlusPreservesSheaf.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Sheafification/PlusPreservesSheaf.lean#L22) (StacksCore): “the canonical map `F ⟶ F⁺` is locally surjective”. References: SGA 3 IV (4.3.11).

## Tag 00WA, a definition

[Tag 00WA](https://stacks.math.columbia.edu/tag/00WA) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Presheaf.IsSeparated`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Presheaf.IsSeparated#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Sheafification/PlusUniversal.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Sheafification/PlusUniversal.lean#L23) (StacksCore): “a presheaf is separated when two sections over `U` whose restrictions along every arrow of a covering sieve agree are equal”. References: SGA 4 II (2.1), “separated presheaf”; SGA 3 IV (4.3.1); SGA 3 IV (4.3.18); SGA 3 XXII (4.1.11); SGA 4 II (2.7); SGA 4 II (3.2).

## Tag 00WB, a theorem

[Tag 00WB](https://stacks.math.columbia.edu/tag/00WB) in the Stacks Project.

**`StacksSheafification.isSeparated_plusObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/SeparatedPlusIsSheaf.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheafification/SeparatedPlusIsSheaf.lean#L53). References: SGA 3 IV (4.3.11), “(i), LP separated”; SGA 4 II (3.2), “2)”.

> **Stacks 00WB(1).** The presheaf `P⁺` is separated.

```lean
theorem isSeparated_plusObj : IsSeparated J (J.plusObj P)
```

**`StacksSheafification.isSheaf_plusObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/SeparatedPlusIsSheaf.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheafification/SeparatedPlusIsSheaf.lean#L58).

> **Stacks 00WB(2), first half.** If `P` is separated then `P⁺` is a sheaf.

```lean
theorem isSheaf_plusObj (hP : IsSeparated J P) : Presheaf.IsSheaf J (J.plusObj P)
```

**`StacksSheafification.injective_toPlus_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/SeparatedPlusIsSheaf.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheafification/SeparatedPlusIsSheaf.lean#L64). References: SGA 3 IV (4.3.11), “(iv), mono part”; SGA 4 II (3.2), “3) separated ⇒ mono”.

> **Stacks 00WB(2), second half.** If `P` is separated then the canonical map
> `P → P⁺` is injective on sections over every object.

```lean
theorem injective_toPlus_app (hP : IsSeparated J P) (X : C) :
    Function.Injective ((J.toPlus P).app (op X))
```

**`StacksSheafification.isIso_toPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/SeparatedPlusIsSheaf.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheafification/SeparatedPlusIsSheaf.lean#L71). References: SGA 3 IV (4.3.11), “(ii)”; SGA 4 II (3.2), “4) (ii) ⇒ (i)”.

> **Stacks 00WB(3).** If `P` is a sheaf then the canonical map `P → P⁺` is an
> isomorphism.

```lean
theorem isIso_toPlus (hP : Presheaf.IsSheaf J P) : IsIso (J.toPlus P)
```

**`StacksSheafification.isSheaf_plusObj_plusObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/SeparatedPlusIsSheaf.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheafification/SeparatedPlusIsSheaf.lean#L76). References: SGA 4 II (3.2), “clause 3, special case”.

> **Stacks 00WB(4).** The presheaf `P⁺⁺` is always a sheaf.

```lean
theorem isSheaf_plusObj_plusObj : Presheaf.IsSheaf J (J.plusObj (J.plusObj P))
```

## Tag 00WG, a definition

[Tag 00WG](https://stacks.math.columbia.edu/tag/00WG) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.GrothendieckTopology.sheafify`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.sheafify#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch07.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch07.lean#L33) (StacksFrontier): “the sheaf F^# := F^\{++}”. References: SGA 3 IV (4.3.14); SGA 3 IV (4.3.15); SGA 3 VIB (8.1); SGA 4 II (3.5), “the sheaf F^# = LLF”.
- [`CategoryTheory.GrothendieckTopology.toSheafify`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.toSheafify#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch07.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch07.lean#L34) (StacksFrontier): “the canonical map F → F^#”. References: SGA 4 II (3.5), “canonical map F → aF”.

## Tag 00WH, a proposition

[Tag 00WH](https://stacks.math.columbia.edu/tag/00WH) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.sheafifyLift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.sheafifyLift#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Sheafification/SheafificationAdjoint.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Sheafification/SheafificationAdjoint.lean#L25) (StacksCore): “the lift `γ : F^# ⟶ Q` of a map `η : F ⟶ Q` into a sheaf”.
- [`CategoryTheory.toSheafify_sheafifyLift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.toSheafify_sheafifyLift#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Sheafification/SheafificationAdjoint.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Sheafification/SheafificationAdjoint.lean#L27) (StacksCore): “the lift factors `η` through the canonical map `F ⟶ F^#`”. References: EGA 0 (3.5.6), “partial”.
- [`CategoryTheory.sheafifyLift_unique`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.sheafifyLift_unique#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Sheafification/SheafificationAdjoint.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Sheafification/SheafificationAdjoint.lean#L29) (StacksCore): “the lift is the unique such factorization”. References: EGA 0 (3.5.6), “partial”.

## Tag 0H7J, an example

[Tag 0H7J](https://stacks.math.columbia.edu/tag/0H7J) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.constantSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.constantSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Sheafification/ConstantSheafMapsOut.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheafification/ConstantSheafMapsOut.lean#L26) (StacksFrontier): “the constant sheaf”. References: EGA 0 (15.2.1), “partial”; EGA 0 (3.6.1); SGA 4 IV (11.1.5); SGA 4 IV (2.7.5); SGA 4 IV (4.3.4); SGA 4 IX (2.0); SGA 4 VII (2.1), “partial”; SGA 4½ Arcata (2.2.1); SGA 4½ Arcata (4.3.2).
- [`CategoryTheory.constantSheafΓAdj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.constantSheafΓAdj#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Sheafification/ConstantSheafMapsOut.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheafification/ConstantSheafMapsOut.lean#L27) (StacksFrontier): “maps out of the constant sheaf”.

## Tag 00WI, a lemma

[Tag 00WI](https://stacks.math.columbia.edu/tag/00WI) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Sheaf.sheafifyCocone`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.sheafifyCocone#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Limits.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Limits.lean#L23) (StacksCore): “the colimit of a diagram of sheaves, obtained by sheafifying a cocone of the underlying diagram of presheaves”.
- [`CategoryTheory.Sheaf.isColimitSheafifyCocone`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.isColimitSheafifyCocone#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Limits.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Limits.lean#L25) (StacksCore): “the sheafification of a presheaf colimit cocone is a colimit cocone of sheaves, so the colimit of a diagram of sheaves exists and is the sheafification of the colimit taken in presheaves”. References: SGA 3 IV (4.4.1), “more general”; SGA 4 II (4.1), “partial”; SGA 4 II (5.3.1), “special case”.

## Tag 00WJ, a lemma

[Tag 00WJ](https://stacks.math.columbia.edu/tag/00WJ) in the Stacks Project.

**`CategoryTheory.presheafToSheaf_preservesFiniteColimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/PreservesFiniteColimits.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheafification/PreservesFiniteColimits.lean#L45). The attribute's comment: “Sheafification `PSh(C) → Sh(C)`, `F ↦ F^#`, is exact: it commutes with finite limits and with finite colimits. This is the right-exact half; the left-exact half is `presheafToSheaf_preservesFiniteLimits`.”. References: SGA 3 IV (4.4.1), “(iii)”; SGA 4 II (4.1), “partial, special case”; SGA 7 VI (3.1(a)), “partial”.

> Sheafification `presheafToSheaf J A : PSh(C) ⥤ Sh(C)`, `F ↦ F^#`, preserves finite colimits,
> for sheaves with values in any category `A` in which sheafification exists.

```lean
noncomputable instance presheafToSheaf_preservesFiniteColimits
    {C : Type u₁} [Category.{v₁} C] (J : GrothendieckTopology C)
    (A : Type u₂) [Category.{v₂} A] [HasWeakSheafify J A] :
    PreservesFiniteColimits (presheafToSheaf J A)
```

**`presheafToSheaf_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/PreservesFiniteLimits.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheafification/PreservesFiniteLimits.lean#L90). The attribute's comment: “Sheafification `PSh(C) → Sh(C)`, `F ↦ F^#`, is exact: it commutes with finite limits and with finite colimits. This is the left-exact half; the right-exact half is `CategoryTheory.presheafToSheaf_preservesFiniteColimits`.”. References: SGA 3 IV (4.3.16), “partial”; SGA 3 IV (4.4.1), “more general”; SGA 4 II (3.4), “more general”; SGA 4 II (4.1), “Clause 1”; SGA 4 II (6.3.3), “more general”.

> **Stacks 00WJ**, left-exact half. Let `(C, J)` be a site and let `A` be a concrete category in
> which the plus construction `F ↦ F^+` can be carried out and whose finite limits and coverings
> colimits are computed on underlying sets. Then sheafification
> `presheafToSheaf J A : PSh(C) ⥤ Sh(C)`, `F ↦ F^#`, preserves finite limits. Together with
> `CategoryTheory.presheafToSheaf_preservesFiniteColimits`, which holds because `F ↦ F^#` is a left
> adjoint, this says that sheafification is exact.

```lean
public theorem presheafToSheaf_preservesFiniteLimits
    {C : Type u} [Category.{v} C] (J : GrothendieckTopology C) (A : Type w) [Category.{t} A]
    {FA : A → A → Type*} {CA : A → Type t} [∀ X Y, FunLike (FA X Y) (CA X) (CA Y)]
    [ConcreteCategory.{t} A FA]
    [∀ (P : Cᵒᵖ ⥤ A) (X : C) (S : J.Cover X), HasMultiequalizer (S.index P)]
    [∀ X : C, HasColimitsOfShape (J.Cover X)ᵒᵖ A]
    [∀ X : C, PreservesColimitsOfShape (J.Cover X)ᵒᵖ (forget A)]
    [∀ {X : C} (S : J.Cover X), PreservesLimitsOfShape (WalkingMulticospan S.shape) (forget A)]
    [∀ X : C, Small.{t, max u v} (J.Cover X)ᵒᵖ]
    [(forget A).ReflectsIsomorphisms] [HasFiniteLimits A] [PreservesFiniteLimits (forget A)] :
    PreservesFiniteLimits (presheafToSheaf J A)
```

## Tag 00WK, a lemma

[Tag 00WK](https://stacks.math.columbia.edu/tag/00WK) in the Stacks Project.

**`exists_local_description`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/SectionsLocalDescription.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheafification/SectionsLocalDescription.lean#L123). The attribute's comment: “(1)”.

> **Statement 1 (existence of a local description).**
> Every section `s` of the sheafification `P♯` over `U` admits, on some covering
> `{U_i → U}` of `U`, a description by local sections `s_i ∈ P(U_i)` of the original
> presheaf such that `s|_{U_i} = θ²(s_i)` (condition (1)) and the `s_i` agree on the
> overlaps `U_i ×_U U_j` after applying `θ²` (condition (2)).
>
> Proof strategy:
> * The canonical map `θ² = J.toSheafify P` is *locally surjective* (Mathlib
>   instance `Presheaf.isLocallySurjective_toSheafify`).  Hence the *image sieve*
>   `S := Presheaf.imageSieve θ² s` of `s` is a covering of `U`
>   (`Presheaf.IsLocallySurjective.imageSieve_mem`).  Take `𝒰 := ⟨S, _⟩ : J.Cover U`.
> * For each leg `I : 𝒰.Arrow`, membership `I.hf : S.arrows I.f` unfolds, for the
>   image sieve, to `∃ t : P(I.Y), θ².app _ t = (sheafify P).map I.f.op s`.  Use
>   `choose` to pick `s_ I := t` and the witness `hs_ I`.
> * Condition (1) `IsLocalDescription` is exactly `(hs_ I).symm`.
> * Condition (2) `MatchingOnOverlaps` needs **no** sheaf-separatedness: rewrite
>   `θ²(s_ I) = (sheafify P).map I.f.op s` and `θ²(s_ I') = (sheafify P).map I'.f.op s`
>   (the `hs_` witnesses), collapse the two restrictions via functoriality
>   (`Functor.map_comp_apply`, `op_comp`), and use `pullback.condition`
>   (`fst ≫ I.f = snd ≫ I'.f`) to identify the two composite restrictions.

```lean
theorem exists_local_description {U : C} (s : (J.sheafify P).obj (op U)) :
    ∃ (𝒰 : J.Cover U) (s_ : ∀ I : 𝒰.Arrow, P.obj (op I.Y)),
      IsLocalDescription J P 𝒰 s s_ ∧ MatchingOnOverlaps J P 𝒰 s_
```

**`exists_unique_glue`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/SectionsLocalDescription.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheafification/SectionsLocalDescription.lean#L148). The attribute's comment: “(2)”.

> **Statement 2 (converse: gluing and uniqueness).**
> Conversely, given any covering `{U_i → U}` and local sections `s_i ∈ P(U_i)`
> satisfying the overlap condition (2), there is a **unique** section `s ∈ P♯(U)`
> with `s|_{U_i} = θ²(s_i)` for all `i` (condition (1)).
>
> Proof strategy:
> * Build a compatible family `x : Meq F 𝒰` for `F := J.sheafify P` with
>   `x I = θ².app (op I.Y) (s_ I)`; its `condition` is exactly `matching_relation`
>   (the overlap condition transported to every `Relation`).
> * `F` is a sheaf (`J.sheafify_isSheaf P`), so by `sheaf_glue_meq` the family `x`
>   glues to a unique section `t` with `F.map I.f.op t = x I = θ²(s_ I)`, i.e.
>   satisfying `IsLocalDescription`; uniqueness is the `∃!` part of `sheaf_glue_meq`.

```lean
theorem exists_unique_glue {U : C} (𝒰 : J.Cover U)
    (s_ : ∀ I : 𝒰.Arrow, P.obj (op I.Y)) (h : MatchingOnOverlaps J P 𝒰 s_) :
    ∃! s : (J.sheafify P).obj (op U), IsLocalDescription J P 𝒰 s s_
```

## Tag 0H6Y, a lemma

[Tag 0H6Y](https://stacks.math.columbia.edu/tag/0H6Y) in the Stacks Project.

**`CategoryTheory.Presheaf.isIso_presheafToSheaf_map_of_hasEnoughObjects_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyBijective.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyBijective.lean#L80). The attribute's comment: “Bijectivity of a map of presheaves on a family of objects covering every object makes the induced map of sheafifications an isomorphism.”.

> Let `φ : F ⟶ G` be a map of presheaves on a site `(C, J)`. If every object of `C` has a
> covering by objects `U` for which `φ` is bijective on sections over `U`, then the map of
> sheafifications `F^# ⟶ G^#` is an isomorphism.

```lean
theorem isIso_presheafToSheaf_map_of_hasEnoughObjects_bijective
    [HasWeakSheafify J D] [J.WEqualsLocallyBijective D]
    (hB : J.HasEnoughObjects (fun U => Function.Bijective (φ.app (op U)))) :
    IsIso ((presheafToSheaf J D).map φ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.10, Tag 00W1](https://stacks.math.columbia.edu/tag/00W1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
