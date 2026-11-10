---
declaration: section
origin: cited
lean: CategoryTheory.Functor.SieveDescentDatum, CategoryTheory.Functor.FamilyDescentDatum, Pseudofunctor.DescentData', Pseudofunctor.DescentData'.Hom, Pseudofunctor.DescentData'.instCategory, CategoryTheory.Functor.DescentDatum.diagonalPullback_eq_id, CategoryTheory.Functor.DescentDatum.gluing_comp_switchPullback_eq_id, CategoryTheory.Functor.FamilyDescentDatum.pull
statement: formalized
proof: formalized
---

# 8.3 Descent data in fibred categories

Section 8.3 of the Stacks Project, [Tag 02ZC](https://stacks.math.columbia.edu/tag/02ZC). 7 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 11 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 026B, a definition

[Tag 026B](https://stacks.math.columbia.edu/tag/026B) in the Stacks Project.

**`CategoryTheory.Functor.SieveDescentDatum`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/IsStack/SieveDescentDatum.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Descent/IsStack/SieveDescentDatum.lean#L57). The attribute's comment: “(1), sieve-indexed, with no chosen fibre products `U i ×_U U j`”. References: SGA 3 IV (2.1), “descent datum”; SGA 4½ Arcata (1.4.4).

> A descent datum relative to a sieve `R` on `U`: an object of the fibre over `V` for each arrow
> `f : V ⟶ U` of `R`, and for each pair of arrows of `R` and each pair of morphisms `ε`, `ε'` into
> their sources agreeing over `U`, an isomorphism between the chosen pullbacks along `ε` and `ε'` of
> the two attached objects, compatible with composition and with base change.

```lean
structure SieveDescentDatum (p : 𝒳 ⥤ 𝒮) [p.IsFibered] {U : 𝒮} (R : Sieve U)
```

**`CategoryTheory.Functor.FamilyDescentDatum`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/PullbackDescentData.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Descent/PullbackDescentData.lean#L81). The attribute's comment: “The category `DD(𝒰)` for a fibred category: its objects (1), its morphisms (2) and its category structure (3). Indexed by an arbitrary object mapping to two members of the family in place of the chosen fibre products `U i ×_U U i'`, which the two presentations agree over whenever those exist, by `CategoryTheory.Pseudofunctor.DescentData'.descentDataEquivalence`.”. References: SGA 3 IV (2.1), “descent datum”; SGA 1 VIII (7.8), “more general”.

> The category of *descent data relative to a family of morphisms with fixed target*
> `𝒰 = {U i ⟶ U}` for a fibred category `p : 𝒳 ⥤ 𝒮`: an object of the fibre `𝒳_{U i}` for every
> `i`, together with a gluing isomorphism between the two pullbacks of these objects to any object
> `Y` mapping to `U i` and to `U i'` compatibly over `U`, subject to the cocycle condition and to
> compatibility with further base change.

```lean
abbrev FamilyDescentDatum (p : 𝒳 ⥤ 𝒮) [p.IsFibered] {U : 𝒮} (𝒰 : PreZeroHypercover.{w} U)
```

Declarations registered for the tag:

- [`Pseudofunctor.DescentData'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Pseudofunctor.DescentData'#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Descent/DescentData.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Descent/DescentData.lean#L41) (StacksCore): “(1)”.
- [`Pseudofunctor.DescentData'.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Pseudofunctor.DescentData'.Hom#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Descent/DescentData.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Descent/DescentData.lean#L42) (StacksCore): “(2)”.
- [`Pseudofunctor.DescentData'.instCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Pseudofunctor.DescentData'.instCategory#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Descent/DescentData.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Descent/DescentData.lean#L43) (StacksCore): “(3), the category DD(𝒰)”.

## Tag 026C, remarks

[Tag 026C](https://stacks.math.columbia.edu/tag/026C) in the Stacks Project.

**`CategoryTheory.Functor.DescentDatum.diagonalPullback_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/Stack.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/InheritedTopology/Stack.lean#L370). The attribute's comment: “diagonal identity”.

> Let `D` be a descent datum for `p` fibred in groupoids, and `Δ : V i ⟶ Vijk i i i` the
> diagonal. A fibre automorphism `e` of `x i` which is the pullback along `Δ` of each of the three
> gluing isomorphisms of the triple `(i, i, i)` is the identity.

```lean
theorem DescentDatum.diagonalPullback_eq_id
    (D : DescentDatum p V f Vij pr₁ pr₂ hVij Vijk s₁₂ s₂₃ hVijk q₁ q₂ q₃ hq₁ hq₂ hq₃)
    (hp : p.IsFiberedInGroupoids) (i : I) {Δ : V i ⟶ Vijk i i i}
    {hΔ₁ : 𝟙 (V i) = Δ ≫ q₁ i i i} {hΔ₂ : 𝟙 (V i) = Δ ≫ q₂ i i i}
    {hΔ₃ : 𝟙 (V i) = Δ ≫ q₃ i i i}
    {e : D.x i ⟶ D.x i}
    (he : FibreHom p (D.x i) (D.x i) (D.hx i) (D.hx i) e)
    (heij : IsRestrictionOf p Δ hΔ₁ hΔ₂ (D.wi i i i) (D.wj i i i)
      (Restriction.id p (D.x i) (D.hx i)) (Restriction.id p (D.x i) (D.hx i))
      (D.αij i i i) e)
    (hejk : IsRestrictionOf p Δ hΔ₂ hΔ₃ (D.wj i i i) (D.wk i i i)
      (Restriction.id p (D.x i) (D.hx i)) (Restriction.id p (D.x i) (D.hx i))
      (D.αjk i i i) e)
    (heik : IsRestrictionOf p Δ hΔ₁ hΔ₃ (D.wi i i i) (D.wk i i i)
      (Restriction.id p (D.x i) (D.hx i)) (Restriction.id p (D.x i) (D.hx i))
      (D.αik i i i) e) :
    e = 𝟙 (D.x i)
```

**`CategoryTheory.Functor.DescentDatum.gluing_comp_switchPullback_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/Stack.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/InheritedTopology/Stack.lean#L397). The attribute's comment: “flip identity”.

> Let `D` be a descent datum and `Δ₁₃ : Vij i j ⟶ Vijk i j i` the morphism whose composites
> with the three projections are `pr₁ i j`, `pr₂ i j` and `pr₁ i j`. If `σφ` is the pullback along
> `Δ₁₃` of the `(j, k)` gluing isomorphism of the triple `(i, j, i)`, then `φ i j ≫ σφ = 𝟙`.

```lean
theorem DescentDatum.gluing_comp_switchPullback_eq_id
    (D : DescentDatum p V f Vij pr₁ pr₂ hVij Vijk s₁₂ s₂₃ hVijk q₁ q₂ q₃ hq₁ hq₂ hq₃)
    (i j : I) {Δ₁₃ : Vij i j ⟶ Vijk i j i}
    {hΔ₁ : pr₁ i j = Δ₁₃ ≫ q₁ i j i} {hΔ₂ : pr₂ i j = Δ₁₃ ≫ q₂ i j i}
    {hΔ₃ : pr₁ i j = Δ₁₃ ≫ q₃ i j i}
    {σφ : (D.xrji i j).pt ⟶ (D.xrij i j).pt}
    (hσφ : FibreHom p (D.xrji i j).pt (D.xrij i j).pt
      (D.xrji i j).hpt (D.xrij i j).hpt σφ)
    (hij : IsRestrictionOf p Δ₁₃ hΔ₁ hΔ₂ (D.wi i j i) (D.wj i j i)
      (D.xrij i j) (D.xrji i j) (D.αij i j i) (D.φ i j))
    (hji : IsRestrictionOf p Δ₁₃ hΔ₂ hΔ₃ (D.wj i j i) (D.wk i j i)
      (D.xrji i j) (D.xrij i j) (D.αjk i j i) σφ)
    (hik : IsRestrictionOf p Δ₁₃ hΔ₁ hΔ₃ (D.wi i j i) (D.wk i j i)
      (D.xrij i j) (D.xrij i j) (D.αik i j i) (𝟙 (D.xrij i j).pt)) :
    D.φ i j ≫ σφ = 𝟙 (D.xrij i j).pt
```

## Tag 02ZD, a lemma

[Tag 02ZD](https://stacks.math.columbia.edu/tag/02ZD) in the Stacks Project.

**`CategoryTheory.Functor.FamilyDescentDatum.pull`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/PullbackDescentData.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Descent/PullbackDescentData.lean#L95). The attribute's comment: “(1) the descent datum `(g i ^* Y (α i), (g i × g i') ^* φ (α i) (α i'))`”.

> **Stacks 02ZD (1).**
> The descent datum relative to `𝒰 = {U i ⟶ U}` obtained from a descent datum `(Y j, φ j j')`
> relative to `𝒱 = {V j ⟶ V}` by pulling back along a morphism of families `Φ = (α, h, g)`: its
> object over `U i` is the chosen pullback `g i ^* Y (α i)`, and its gluing morphisms are those of
> `(Y j, φ j j')` pulled back along the `g i`.

```lean
noncomputable def pull (Φ : 𝒰.HomOver 𝒱 h) (D : FamilyDescentDatum p 𝒱) :
    FamilyDescentDatum p 𝒰
```

**`CategoryTheory.Functor.FamilyDescentDatum.pullFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/PullbackDescentData.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Descent/PullbackDescentData.lean#L131). The attribute's comment: “(2) the functor from descent data relative to `𝒱` to descent data relative to `𝒰`”.

> **Stacks 02ZD (2).**
> Pulling back descent data along a morphism of families `Φ = (α, h, g)` from `𝒰` to `𝒱` is a
> functor from the category of descent data relative to `𝒱` to the category of descent data
> relative to `𝒰`.

```lean
noncomputable def pullFunctor (Φ : 𝒰.HomOver 𝒱 h) :
    FamilyDescentDatum p 𝒱 ⥤ FamilyDescentDatum p 𝒰
```

**`CategoryTheory.Functor.FamilyDescentDatum.pullFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/PullbackDescentData.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Descent/PullbackDescentData.lean#L155). The attribute's comment: “(3) for two morphisms of families over one and the same `h : U ⟶ V`”.

> **Stacks 02ZD (3).**
> Two morphisms of families `Φ = (α, h, g)` and `Φ' = (α', h, g')` from `𝒰` to `𝒱` lying over one
> and the same morphism `h : U ⟶ V` of the targets induce canonically isomorphic functors on
> descent data. The component of the isomorphism at a descent datum `(Y j, φ j j')` and an index
> `i` is the gluing isomorphism of that datum between `g i ^* Y (α i)` and `g' i ^* Y (α' i)`.

```lean
noncomputable def pullFunctorIso (Φ Φ' : 𝒰.HomOver 𝒱 h) : pullFunctor p Φ ≅ pullFunctor p Φ'
```

**`CategoryTheory.Functor.FamilyDescentDatum.pullFunctorIsoOfEq`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/PullbackDescentData.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Descent/PullbackDescentData.lean#L173). The attribute's comment: “(3) for morphisms of families over `h` and over `h'` with `h' = h`, as in Stacks”.

> **Stacks 02ZD (3)**, with the hypothesis `h = h'` on the two morphisms of targets stated as
> such: morphisms of families `Φ` over `h` and `Φ'` over `h'` with `h' = h` induce canonically
> isomorphic functors on descent data.

```lean
noncomputable def pullFunctorIsoOfEq {h' : U ⟶ V} (Φ : 𝒰.HomOver 𝒱 h) (Φ' : 𝒰.HomOver 𝒱 h')
    (hh : h' = h) : pullFunctor p Φ ≅ pullFunctor p Φ'
```

Declarations registered for the tag:

- [`Pseudofunctor.DescentData.pullFunctorObj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Pseudofunctor.DescentData.pullFunctorObj#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Descent/DescentData.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Descent/DescentData.lean#L84) (StacksCore): “(1)”.
- [`Pseudofunctor.DescentData.pullFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Pseudofunctor.DescentData.pullFunctor#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Descent/DescentData.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Descent/DescentData.lean#L85) (StacksCore): “(2)”.
- [`Pseudofunctor.DescentData.pullFunctorIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Pseudofunctor.DescentData.pullFunctorIso#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Descent/DescentData.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Descent/DescentData.lean#L86) (StacksCore): “(3), with `h = h'` built in by sharing `p`”.

## Tag 02ZE, a definition

[Tag 02ZE](https://stacks.math.columbia.edu/tag/02ZE) in the Stacks Project.

**`CategoryTheory.Functor.FamilyDescentDatum.pullFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/PullbackDescentData.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Descent/PullbackDescentData.lean#L131).

> **Stacks 02ZD (2).**
> Pulling back descent data along a morphism of families `Φ = (α, h, g)` from `𝒰` to `𝒱` is a
> functor from the category of descent data relative to `𝒱` to the category of descent data
> relative to `𝒰`.

```lean
noncomputable def pullFunctor (Φ : 𝒰.HomOver 𝒱 h) :
    FamilyDescentDatum p 𝒱 ⥤ FamilyDescentDatum p 𝒰
```

Declarations registered for the tag:

- [`Pseudofunctor.DescentData.pullFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Pseudofunctor.DescentData.pullFunctor#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Descent/DescentData.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Descent/DescentData.lean#L91) (StacksCore).

## Tag 026E, a definition

[Tag 026E](https://stacks.math.columbia.edu/tag/026E) in the Stacks Project.

**`CategoryTheory.Functor.SieveDescentDatum.ofFiber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/IsStack/OfFiber.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Descent/IsStack/OfFiber.lean#L55). The attribute's comment: “(1) and (2) are one construction, read at two sieves: the trivial descent datum `(X, id_X)` on `{𝟙 U}` is this datum at the sieve generated by `𝟙 U`, and the canonical descent datum `(f_i^* X, can)` on `{f_i : U_i → U}` is this datum at the sieve that family generates, with `can` the canonical comparison `CategoryTheory.Functor.pullbackFiberComparison`.”. References: SGA 3 IV (2.1), “canonical descent datum”.

> The descent datum of an object `x` of the fibre over `U`: its chosen pullbacks, glued by the
> canonical comparisons of their iterated chosen pullbacks.

```lean
noncomputable def ofFiber (x : p.Fiber U) (R : Sieve U) : SieveDescentDatum p R
```

**`CategoryTheory.Functor.SieveDescentDatum.IsEffective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/IsStack/SieveDescentDatum.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Descent/IsStack/SieveDescentDatum.lean#L111). The attribute's comment: “(3), effectivity of a descent datum, stated as the existence of an object `x` of the fibre over `U` and a cartesian morphism from each object of the datum to `x` compatible with the gluing isomorphisms, in place of an isomorphism with `(f_i^* X, can)`.”. References: SGA 3 IV (3.5.1).

> A descent datum is effective when it comes from an object `x` of the fibre over `U`: there is a
> cartesian morphism from each of its objects to `x`, compatibly with the gluing isomorphisms.

```lean
def IsEffective : Prop
```

Declarations registered for the tag:

- [`Pseudofunctor.DescentData.ofObj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Pseudofunctor.DescentData.ofObj#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Descent/DescentData.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Descent/DescentData.lean#L60) (StacksCore): “(1) and (2)”.
- [`Pseudofunctor.toDescentData`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Pseudofunctor.toDescentData#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Descent/DescentData.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Descent/DescentData.lean#L61) (StacksCore): “(2), as a functor 𝒮_U ⥤ DD(𝒰)”.
- [`Functor.essImage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Functor.essImage#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Descent/DescentData.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Descent/DescentData.lean#L62) (StacksCore): “(3), effectivity is `(F.toDescentData f).essImage`”.

## Tag 026D, a lemma

[Tag 026D](https://stacks.math.columbia.edu/tag/026D) in the Stacks Project.

**`CategoryTheory.Functor.pullbackFiberComparison_comp_compIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stackification/StageThreeStack.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stackification/StageThreeStack.lean#L112). The attribute's comment: “`can_ij = (α_{pr₁, f_j})_X ∘ (α_{pr₀, f_i})_X⁻¹`, where `can` is the gluing isomorphism `pullbackFiberComparison` of the canonical descent datum of Stacks 026E (2); stated as the commuting square, with `α⁻¹` the contraction `pullbackFiberCompIso` of Stacks 02XO and `f_i ∘ pr₀ = f_j ∘ pr₁` carried by `pullbackFiberCongr`”.

> The comparison of two chosen pullbacks of a chosen pullback is the comparison of the two
> chosen pullbacks along the composites.

```lean
theorem pullbackFiberComparison_comp_compIso {T : 𝒮} (y : p.Fiber T) {V W Z : 𝒮} {g : V ⟶ T}
    {g' : W ⟶ T} (ε : Z ⟶ V) (ε' : Z ⟶ W) (heq : ε ≫ g = ε' ≫ g') :
    (pullbackFiberComparison y ε ε' heq).hom ≫ (pullbackFiberCompIso y g' ε').hom =
      (pullbackFiberCompIso y g ε).hom ≫ (pullbackFiberCongr y heq).hom
```

Declarations registered for the tag:

- [`Pseudofunctor.DescentData.ofObj_hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Pseudofunctor.DescentData.ofObj_hom#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Descent/DescentData.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Descent/DescentData.lean#L51) (StacksCore).

## Tag 0GEA, a lemma

[Tag 0GEA](https://stacks.math.columbia.edu/tag/0GEA) in the Stacks Project.

**`CategoryTheory.Functor.isEquivalence_toFamilyDescentDatum_of_homOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/OfRefinement.lean, line 548](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Descent/OfRefinement.lean#L548).

> **Stacks 0GEA.**
> Let `𝒱 = {V j ⟶ U} ⟶ 𝒰 = {U i ⟶ U}` be a morphism of families of morphisms with fixed target
> given by `𝟙 U`, a reindexing `α : J → I` and morphisms `V j ⟶ U (α j)`, and let `p` be a fibred
> category. Assume that the fibre products `U i₁ ×_U U i₂`, `U i ×_U V j` and
> `U i₁ ×_U U i₂ ×_U V j` exist, that `𝒮_U ⟶ DD(𝒱)` is an equivalence, that `𝒮_{U i} ⟶ DD(𝒱_i)`
> is fully faithful for every `i`, and that `𝒮_{U i₁ ×_U U i₂} ⟶ DD(𝒱_{i₁i₂})` is faithful for
> every `i₁, i₂`, where `𝒱_i` and `𝒱_{i₁i₂}` are the base changes of `𝒱`. Then `𝒮_U ⟶ DD(𝒰)` is
> an equivalence.

```lean
theorem isEquivalence_toFamilyDescentDatum_of_homOver {p : 𝒳 ⥤ C} [p.IsFibered] {U : C}
    {𝒰 : PreZeroHypercover.{w} U} {𝒱 : PreZeroHypercover.{w'} U} (Φ : 𝒱.HomOver 𝒰 (𝟙 U))
    [∀ i₁ i₂, HasPullback (𝒰.f i₁) (𝒰.f i₂)]
    [∀ i j, HasPullback (𝒰.f i) (𝒱.f j)]
    [∀ i₁ i₂ j, HasPullback (pullback.fst (𝒰.f i₁) (𝒰.f i₂) ≫ 𝒰.f i₁) (𝒱.f j)]
    (h₂ : (toFamilyDescentDatum p 𝒱).IsEquivalence)
    (h₃ : ∀ i, Nonempty (toFamilyDescentDatum p (𝒱.pullback₁ (𝒰.f i))).FullyFaithful)
    (h₄ : ∀ i₁ i₂, (toFamilyDescentDatum p
      (𝒱.pullback₁ (pullback.fst (𝒰.f i₁) (𝒰.f i₂) ≫ 𝒰.f i₁))).Faithful) :
    (toFamilyDescentDatum p 𝒰).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 8.3, Tag 02ZC](https://stacks.math.columbia.edu/tag/02ZC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
