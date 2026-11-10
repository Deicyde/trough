---
declaration: section
origin: cited
lean: CategoryTheory.SpectralSequence.Ungraded, CategoryTheory.SpectralSequence.TowerData.step_Z_unique, CategoryTheory.SpectralSequence.TowerData.step_B_unique, CategoryTheory.SpectralSequence.pageIsoSubquotient, CategoryTheory.SpectralSequence.Z_add_one_self, CategoryTheory.SpectralSequence.B_add_one_self, CategoryTheory.SpectralSequence, CategoryTheory.SpectralSequence.Hom
statement: formalized
proof: formalized
---

# 12.20 Spectral sequences

Section 12.20 of the Stacks Project, [Tag 011M](https://stacks.math.columbia.edu/tag/011M). 2 tags here are carried by 14 declarations of the repository (all in StacksCore) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 011N, a definition

[Tag 011N](https://stacks.math.columbia.edu/tag/011N) in the Stacks Project.

**`CategoryTheory.SpectralSequence.Ungraded`**, an abbrev in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/SpectralSequence/Basic.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/SpectralSequence/Basic.lean#L63). The attribute's comment: “(1) the ungraded case: `d_r : E_r → E_r`, `E_{r+1} ≅ Ker(d_r)/Im(d_r)`”.

> Stacks' ungraded spectral sequences `(E_r, d_r)_{r ≥ r₀}` in `C`: `E_r ∈ C`,
> `d_r : E_r → E_r` with `d_r ∘ d_r = 0`, and `E_{r+1} ≅ Ker(d_r)/Im(d_r)`. This is Mathlib's
> `SpectralSequence` for the shape `ComplexShape.refl Unit` on every page: a homological complex of
> that shape is one object `X ()` with one differential `d () () : X () ⟶ X ()` squaring to zero.
> Stacks' `(E_r, d_r)_{r ≥ 1}` is `r₀ = 1`.

```lean
abbrev Ungraded
```

**`CategoryTheory.SpectralSequence.TowerData.step_Z_unique`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/SpectralSequence/Tower.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/SpectralSequence/Tower.lean#L303). The attribute's comment: “`Z_{r+1}`: the unique `X` with `B_r ⊆ X ⊆ Z_r` and `X/B_r = Ker(d_r)` in `Z_r/B_r`”. References: EGA 0 (11.1.1), “(b) Z\_k inverse image”.

> Stacks' characterisation of `Z_{r+1}` at the level of `E_{r₀}`: it is the unique
> subobject `X` with `B_r ⊆ X ⊆ Z_r` whose image in `E_r = Z_r/B_r` is `Ker(d_r)`.

```lean
lemma step_Z_unique {X : Subobject ((E.page r₀).X pq)} (hB : T.B ≤ X) (hZ : X ≤ T.Z)
    (h : (Subobject.exists T.q).obj ((Subobject.pullback T.Z.arrow).obj X) =
      kernelSubobject ((E.pageOfNat k).d pq ((c (r₀ + k)).next pq))) :
    X = T.step.Z
```

**`CategoryTheory.SpectralSequence.TowerData.step_B_unique`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/SpectralSequence/Tower.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/SpectralSequence/Tower.lean#L313). The attribute's comment: “`B_{r+1}`: the unique `X` with `B_r ⊆ X ⊆ Z_r` and `X/B_r = Im(d_r)` in `Z_r/B_r`”. References: EGA 0 (11.1.1), “(b) B\_k inverse image”.

> Stacks' characterisation of `B_{r+1}` at the level of `E_{r₀}`: it is the unique
> subobject `X` with `B_r ⊆ X ⊆ Z_r` whose image in `E_r = Z_r/B_r` is `Im(d_r)`.

```lean
lemma step_B_unique {X : Subobject ((E.page r₀).X pq)} (hB : T.B ≤ X) (hZ : X ≤ T.Z)
    (h : (Subobject.exists T.q).obj ((Subobject.pullback T.Z.arrow).obj X) =
      imageSubobject ((E.pageOfNat k).d ((c (r₀ + k)).prev pq) pq)) :
    X = T.step.B
```

**`CategoryTheory.SpectralSequence.pageIsoSubquotient`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/SpectralSequence/Tower.lean, line 550](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/SpectralSequence/Tower.lean#L550). The attribute's comment: “the towers `B_r ⊆ Z_r ⊆ E_{r₀}` with `E_r = Z_r/B_r`, for any shape family and `r₀`”.

> Stacks 011N: `E_r = Z_r/B_r`, for every `r ≥ r₀`.

```lean
noncomputable def pageIsoSubquotient (r : ℤ) (hr : r₀ ≤ r := by lia) :
    (E.page r).X pq ≅ cokernel (Subobject.ofLE (E.B pq r) (E.Z pq r) (E.B_le_Z pq r))
```

**`CategoryTheory.SpectralSequence.Z_add_one_self`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/SpectralSequence/Tower.lean, line 612](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/SpectralSequence/Tower.lean#L612). The attribute's comment: “`Z_2 = Ker(d_1)`, i.e. `Z_{r₀+1} = Ker(d_{r₀})`”.

> Stacks 011N's base step: `Z_2 = Ker(d_1)`, i.e. `Z_{r₀+1} = Ker(d_{r₀})`.

```lean
lemma Z_add_one_self :
    E.Z pq (r₀ + 1) = kernelSubobject ((E.page r₀).d pq ((c r₀).next pq))
```

**`CategoryTheory.SpectralSequence.B_add_one_self`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/SpectralSequence/Tower.lean, line 618](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/SpectralSequence/Tower.lean#L618). The attribute's comment: “`B_2 = Im(d_1)`, i.e. `B_{r₀+1} = Im(d_{r₀})`”. References: EGA 0 (11.1.1), “(b) B\_\{r+1}=Im(d\_r)”.

> Stacks 011N's base step: `B_2 = Im(d_1)`, i.e. `B_{r₀+1} = Im(d_{r₀})`.

```lean
lemma B_add_one_self :
    E.B pq (r₀ + 1) = imageSubobject ((E.page r₀).d ((c r₀).prev pq) pq)
```

Declarations registered for the tag:

- [`CategoryTheory.SpectralSequence`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.SpectralSequence#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/SpectralSequence/Basic.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/SpectralSequence/Basic.lean#L48) (StacksCore): “(1) `(E_r, d_r)_{r ≥ r₀}` with `E_{r+1} ≅ Ker(d_r)/Im(d_r)`; any shapes”. References: EGA 0 (11.1.1), “more general”.
- [`CategoryTheory.SpectralSequence.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.SpectralSequence.Hom#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/SpectralSequence/Basic.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/SpectralSequence/Basic.lean#L50) (StacksCore): “(2) `f_r : E_r ⟶ E'_r` commuting with `d_r`, `f_{r+1}` induced by `f_r`”. References: EGA 0 (11.1.2), “partial”.

## Tag 011O, a definition

[Tag 011O](https://stacks.math.columbia.edu/tag/011O) in the Stacks Project.

**`CategoryTheory.SpectralSequence.limitObj`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/SpectralSequence/Tower.lean, line 810](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/SpectralSequence/Tower.lean#L810). The attribute's comment: “(1) limit `E_∞ = Z_∞/B_∞` when `⋂ Z_r` and `⋃ B_r` exist”.

> Stacks 011O (1): if `Z_∞ = ⋂ Z_r` and `B_∞ = ⋃ B_r` exist as subobjects of `E_{r₀}`, the
> limit of the spectral sequence at `pq` is `E_∞ = Z_∞/B_∞`.

```lean
noncomputable def limitObj (hZ : IsGLB (Set.range (E.Z pq)) Zinf)
    (hB : IsLUB (Set.range (E.B pq)) Binf) : C
```

**`CategoryTheory.SpectralSequence.isGLB_range_Z`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/SpectralSequence/Tower.lean, line 834](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/SpectralSequence/Tower.lean#L834). The attribute's comment: “(1), stabilising case: `Z_∞ = ⋂ Z_r` exists and is `Z_{rMin}`”.

> Stacks 011O (1): `Z_∞ = ⋂ Z_r` exists, and is `Z_{rMin}`, when the pages stabilise.

```lean
theorem isGLB_range_Z : IsGLB (Set.range (E.Z pq)) (E.Z pq (E.rMin pq))
```

**`CategoryTheory.SpectralSequence.isLUB_range_B`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/SpectralSequence/Tower.lean, line 843](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/SpectralSequence/Tower.lean#L843). The attribute's comment: “(1), stabilising case: `B_∞ = ⋃ B_r` exists and is `B_{rMin}`”.

> Stacks 011O (1): `B_∞ = ⋃ B_r` exists, and is `B_{rMin}`, when the pages stabilise.

```lean
theorem isLUB_range_B : IsLUB (Set.range (E.B pq)) (E.B pq (E.rMin pq))
```

**`CategoryTheory.SpectralSequence.pageInfinityIsoSubquotient`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/SpectralSequence/Tower.lean, line 852](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/SpectralSequence/Tower.lean#L852). The attribute's comment: “(1), stabilising case: `pageInfinity ≅ Z_{rMin}/B_{rMin}`”.

> Stacks 011O (1): `E_∞ = Z_∞/B_∞`, where `E_∞` is the stable page `pageInfinity`.

```lean
noncomputable def pageInfinityIsoSubquotient :
    E.pageInfinity pq ≅
      cokernel (Subobject.ofLE (E.B pq (E.rMin pq)) (E.Z pq (E.rMin pq)) (E.B_le_Z pq _))
```

**`CategoryTheory.SpectralSequence.limitObjIsoPageInfinity`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/SpectralSequence/Tower.lean, line 859](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/SpectralSequence/Tower.lean#L859). The attribute's comment: “(1), stabilising case: the limit `Z_∞/B_∞` is the stable page `pageInfinity`”.

> Stacks 011O (1), stabilising case: the limit `Z_∞/B_∞` is the stable page `pageInfinity`.

```lean
noncomputable def limitObjIsoPageInfinity {Zinf Binf : Subobject ((E.page r₀).X pq)}
    (hZ : IsGLB (Set.range (E.Z pq)) Zinf) (hB : IsLUB (Set.range (E.B pq)) Binf) :
    E.limitObj hZ hB ≅ E.pageInfinity pq
```

**`CategoryTheory.SpectralSequence.DegeneratesAt`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/SpectralSequence/Tower.lean, line 873](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/SpectralSequence/Tower.lean#L873). The attribute's comment: “(2) degeneration at `E_r`: all differentials `d_{r'}`, `r' ≥ r`, vanish”.

> Stacks 011O (2): the spectral sequence degenerates at `E_r` if `d_r, d_{r+1}, …` all
> vanish.

```lean
def DegeneratesAt (r : ℤ) (hr : r₀ ≤ r := by lia) : Prop
```

**`CategoryTheory.SpectralSequence.DegeneratesAt.pageIso`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/SpectralSequence/Tower.lean, line 928](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/SpectralSequence/Tower.lean#L928). The attribute's comment: “remark: degeneration at `E_r` gives `E_r = E_{r+1} = ⋯`”.

> Stacks 011O, remark: under degeneration at `E_r`, `E_r = E_{r+1} = ⋯`: the pages `E_r` and
> `E_{r'}` agree for `r ≤ r'`.

```lean
noncomputable def pageIso (pq : κ) (r' : ℤ) (hr' : r ≤ r' := by lia) :
    (E.page r hr).X pq ≅ (E.page r' (hr.trans hr')).X pq
```

**`CategoryTheory.SpectralSequence.DegeneratesAt.pageInfinityIso`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/SpectralSequence/Tower.lean, line 939](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/SpectralSequence/Tower.lean#L939). The attribute's comment: “remark: degeneration at `E_r` gives `E_r = E_{r+1} = ⋯ = E_∞`”.

> Stacks 011O, remark: if the spectral sequence degenerates at `E_r`, then
> `E_r = E_{r+1} = ⋯ = E_∞`: at every position `pq`, the infinity page is `E_{r'}^{pq}` for every
> `r' ≥ r`.

```lean
noncomputable def pageInfinityIso (pq : κ) (r' : ℤ) (hr' : r ≤ r' := by lia) :
    E.pageInfinity pq ≅ (E.page r' (hr.trans hr')).X pq
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.20, Tag 011M](https://stacks.math.columbia.edu/tag/011M)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
