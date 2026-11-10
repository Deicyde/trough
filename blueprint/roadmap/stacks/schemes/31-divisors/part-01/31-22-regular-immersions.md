---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.isRegularImmersion_iff_of_open, Stacks.AlgebraicGeometry.RegularIdealSheaf.IsRegularImmersion, Stacks.AlgebraicGeometry.RegularIdealSheaf.IsKoszulRegularImmersion, Stacks.AlgebraicGeometry.RegularIdealSheaf.IsH1RegularImmersion, Stacks.AlgebraicGeometry.RegularIdealSheaf.IsQuasiRegularImmersion, Stacks.AlgebraicGeometry.RegularIdealSheaf.isKoszulRegularIdealSheaf_definingIdealOfHom_congr, Stacks.AlgebraicGeometry.RegularIdealSheaf.isH1RegularIdealSheaf_definingIdealOfHom_congr, Stacks.AlgebraicGeometry.RegularIdealSheaf.isQuasiRegularIdealSheaf_definingIdealOfHom_congr
statement: formalized
proof: formalized
---

# 31.22 Regular immersions

Section 31.22 of the Stacks Project, [Tag 0638](https://stacks.math.columbia.edu/tag/0638). 12 tags here are carried by 55 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 063J, a definition

[Tag 063J](https://stacks.math.columbia.edu/tag/063J) in the Stacks Project.

**`Stacks.AlgebraicGeometry.isRegularImmersion_iff_of_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/RegularOpenIndependence.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/RegularOpenIndependence.lean#L126). The attribute's comment: “part (1): independence of the chosen open”.

> An immersion `i : Z ⟶ X` is regular if and only if, for one — equivalently any — open
> subscheme `U` of `X` through which `i` factors as a closed immersion `j : Z ⟶ U`, the defining
> ideal of `j` is a regular ideal sheaf on `U`.

```lean
theorem isRegularImmersion_iff_of_open {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i]
    (U : X.Opens) (j : Z ⟶ U.toScheme) [IsClosedImmersion j] (hij : j ≫ U.ι = i) :
    IsRegularImmersion i ↔
      IsRegularIdealSheaf U.toScheme.toLocallyRingedSpace.toRingedSpace
        (definingIdealOfHom j)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.IsRegularImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Immersion.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Immersion.lean#L225). The attribute's comment: “part (1): regular immersion”.

> **Stacks tag 063J, part (1).** The immersion `i` is regular when the defining ideal sheaf of
> its canonical closed factor is a regular ideal sheaf.

```lean
def IsRegularImmersion (i : Z ⟶ X) [IsImmersion i] : Prop
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.IsKoszulRegularImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Immersion.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Immersion.lean#L232). The attribute's comment: “part (2): Koszul-regular immersion”. References: SGA 6 VII (1.4), “regular immersion”.

> **Stacks tag 063J, part (2).** The immersion `i` is Koszul-regular when the defining ideal
> sheaf of its canonical closed factor is a Koszul-regular ideal sheaf.

```lean
def IsKoszulRegularImmersion (i : Z ⟶ X) [IsImmersion i] : Prop
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.IsH1RegularImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Immersion.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Immersion.lean#L239). The attribute's comment: “part (3): H₁-regular immersion”.

> **Stacks tag 063J, part (3).** The immersion `i` is `H₁`-regular when the defining ideal
> sheaf of its canonical closed factor is an `H₁`-regular ideal sheaf.

```lean
def IsH1RegularImmersion (i : Z ⟶ X) [IsImmersion i] : Prop
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.IsQuasiRegularImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Immersion.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Immersion.lean#L246). The attribute's comment: “part (4): quasi-regular immersion”. References: EGA IV (16.9.2), “quasi-regular”.

> **Stacks tag 063J, part (4).** The immersion `i` is quasi-regular when the defining ideal
> sheaf of its canonical closed factor is a quasi-regular ideal sheaf.

```lean
def IsQuasiRegularImmersion (i : Z ⟶ X) [IsImmersion i] : Prop
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isKoszulRegularIdealSheaf_definingIdealOfHom_congr`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Independence.lean, line 925](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Independence.lean#L925). The attribute's comment: “part (2): independence of the chosen open, for the restricted defining ideal”.

> **Stacks tag 063J, part (2): independence of the chosen open.** For an immersion `i : Z ⟶ X`
> and two opens of `X` in which `i` is closed, the Koszul-regularity condition of Stacks tag 063D
> on the restriction of the defining ideal sheaf of `i` is the same on both.

```lean
theorem isKoszulRegularIdealSheaf_definingIdealOfHom_congr (i : Z ⟶ X) [IsImmersion i]
    (V V' : X.Opens) (j : Z ⟶ V.toScheme) [IsClosedImmersion j] (hij : j ≫ V.ι = i)
    (j' : Z ⟶ V'.toScheme) [IsClosedImmersion j'] (hij' : j' ≫ V'.ι = i) :
    IsKoszulRegularIdealSheaf V.toScheme.toLocallyRingedSpace.toRingedSpace
        (restrictSubmodule V (definingIdealOfHom i)) ↔
      IsKoszulRegularIdealSheaf V'.toScheme.toLocallyRingedSpace.toRingedSpace
        (restrictSubmodule V' (definingIdealOfHom i))
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isH1RegularIdealSheaf_definingIdealOfHom_congr`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Independence.lean, line 937](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Independence.lean#L937). The attribute's comment: “part (3): independence of the chosen open, for the restricted defining ideal”.

> **Stacks tag 063J, part (3): independence of the chosen open.**

```lean
theorem isH1RegularIdealSheaf_definingIdealOfHom_congr (i : Z ⟶ X) [IsImmersion i]
    (V V' : X.Opens) (j : Z ⟶ V.toScheme) [IsClosedImmersion j] (hij : j ≫ V.ι = i)
    (j' : Z ⟶ V'.toScheme) [IsClosedImmersion j'] (hij' : j' ≫ V'.ι = i) :
    IsH1RegularIdealSheaf V.toScheme.toLocallyRingedSpace.toRingedSpace
        (restrictSubmodule V (definingIdealOfHom i)) ↔
      IsH1RegularIdealSheaf V'.toScheme.toLocallyRingedSpace.toRingedSpace
        (restrictSubmodule V' (definingIdealOfHom i))
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isQuasiRegularIdealSheaf_definingIdealOfHom_congr`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Independence.lean, line 949](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Independence.lean#L949). The attribute's comment: “part (4): independence of the chosen open, for the restricted defining ideal”.

> **Stacks tag 063J, part (4): independence of the chosen open.**

```lean
theorem isQuasiRegularIdealSheaf_definingIdealOfHom_congr (i : Z ⟶ X) [IsImmersion i]
    (V V' : X.Opens) (j : Z ⟶ V.toScheme) [IsClosedImmersion j] (hij : j ≫ V.ι = i)
    (j' : Z ⟶ V'.toScheme) [IsClosedImmersion j'] (hij' : j' ≫ V'.ι = i) :
    IsQuasiRegularIdealSheaf V.toScheme.toLocallyRingedSpace.toRingedSpace
        (restrictSubmodule V (definingIdealOfHom i)) ↔
      IsQuasiRegularIdealSheaf V'.toScheme.toLocallyRingedSpace.toRingedSpace
        (restrictSubmodule V' (definingIdealOfHom i))
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isKoszulRegularImmersion_iff_of_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Independence.lean, line 1005](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Independence.lean#L1005). The attribute's comment: “part (2): independence of the chosen open”.

> **Stacks tag 063J, part (2): independence of the chosen open.** An immersion is
> Koszul-regular exactly when the defining ideal sheaf of its closed factor through *any* open in
> which it is closed is a Koszul-regular ideal sheaf — not only the canonical one.

```lean
theorem isKoszulRegularImmersion_iff_of_open (i : Z ⟶ X) [IsImmersion i]
    (V : X.Opens) (j : Z ⟶ V.toScheme) [IsClosedImmersion j] (hij : j ≫ V.ι = i) :
    IsKoszulRegularImmersion i ↔
      IsKoszulRegularIdealSheaf V.toScheme.toLocallyRingedSpace.toRingedSpace
        (definingIdealOfHom j)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isH1RegularImmersion_iff_of_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Independence.lean, line 1019](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Independence.lean#L1019). The attribute's comment: “part (3): independence of the chosen open”.

> **Stacks tag 063J, part (3): independence of the chosen open.**

```lean
theorem isH1RegularImmersion_iff_of_open (i : Z ⟶ X) [IsImmersion i]
    (V : X.Opens) (j : Z ⟶ V.toScheme) [IsClosedImmersion j] (hij : j ≫ V.ι = i) :
    IsH1RegularImmersion i ↔
      IsH1RegularIdealSheaf V.toScheme.toLocallyRingedSpace.toRingedSpace
        (definingIdealOfHom j)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isQuasiRegularImmersion_iff_of_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Independence.lean, line 1033](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Independence.lean#L1033). The attribute's comment: “part (4): independence of the chosen open”.

> **Stacks tag 063J, part (4): independence of the chosen open.**

```lean
theorem isQuasiRegularImmersion_iff_of_open (i : Z ⟶ X) [IsImmersion i]
    (V : X.Opens) (j : Z ⟶ V.toScheme) [IsClosedImmersion j] (hij : j ≫ V.ι = i) :
    IsQuasiRegularImmersion i ↔
      IsQuasiRegularIdealSheaf V.toScheme.toLocallyRingedSpace.toRingedSpace
        (definingIdealOfHom j)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isKoszulRegularImmersion_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Independence.lean, line 1137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Independence.lean#L1137). The attribute's comment: “part (2): stability under restricting the target to an open”.

> **Stacks tag 063J, part (2): Koszul-regularity survives restricting the target to an
> open.** If `i : Z ⟶ X` is a Koszul-regular immersion then so is its restriction
> `i.resLE V (i ⁻¹ᵁ V) le_rfl : i ⁻¹ᵁ V ⟶ V` to any open `V ⊆ X`.

```lean
theorem isKoszulRegularImmersion_resLE (i : Z ⟶ X) [IsImmersion i]
    (h : IsKoszulRegularImmersion i) (V : X.Opens) :
    IsKoszulRegularImmersion (i.resLE V (i ⁻¹ᵁ V) le_rfl)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isH1RegularImmersion_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Independence.lean, line 1154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Independence.lean#L1154). The attribute's comment: “part (3): stability under restricting the target to an open”.

> **Stacks tag 063J, part (3): `H₁`-regularity survives restricting the target to an
> open.**

```lean
theorem isH1RegularImmersion_resLE (i : Z ⟶ X) [IsImmersion i]
    (h : IsH1RegularImmersion i) (V : X.Opens) :
    IsH1RegularImmersion (i.resLE V (i ⁻¹ᵁ V) le_rfl)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isQuasiRegularImmersion_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Independence.lean, line 1171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/Independence.lean#L1171). The attribute's comment: “part (4): stability under restricting the target to an open”.

> **Stacks tag 063J, part (4): quasi-regularity survives restricting the target to an
> open.**

```lean
theorem isQuasiRegularImmersion_resLE (i : Z ⟶ X) [IsImmersion i]
    (h : IsQuasiRegularImmersion i) (V : X.Opens) :
    IsQuasiRegularImmersion (i.resLE V (i ⁻¹ᵁ V) le_rfl)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isKoszulRegularImmersion_of_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/ZariskiLocal.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/ZariskiLocal.lean#L97). The attribute's comment: “part (2): gluing along an open cover of the target”.

> **Stacks tag 063J, part (2): Koszul-regularity glues along an open cover of the target.**
> If every restriction `i.resLE (V k) (i ⁻¹ᵁ V k) le_rfl` of the immersion `i` over a member of an
> open cover `V` of `X` is a Koszul-regular immersion, then so is `i`.

```lean
theorem isKoszulRegularImmersion_of_resLE
    (h : ∀ k, IsKoszulRegularImmersion (i.resLE (V k) (i ⁻¹ᵁ V k) le_rfl)) :
    IsKoszulRegularImmersion i
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isH1RegularImmersion_of_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/ZariskiLocal.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/ZariskiLocal.lean#L121). The attribute's comment: “part (3): gluing along an open cover of the target”.

> **Stacks tag 063J, part (3): `H₁`-regularity glues along an open cover of the target.**

```lean
theorem isH1RegularImmersion_of_resLE
    (h : ∀ k, IsH1RegularImmersion (i.resLE (V k) (i ⁻¹ᵁ V k) le_rfl)) :
    IsH1RegularImmersion i
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isQuasiRegularImmersion_of_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/ZariskiLocal.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/ZariskiLocal.lean#L145). The attribute's comment: “part (4): gluing along an open cover of the target”.

> **Stacks tag 063J, part (4): quasi-regularity glues along an open cover of the target.**

```lean
theorem isQuasiRegularImmersion_of_resLE
    (h : ∀ k, IsQuasiRegularImmersion (i.resLE (V k) (i ⁻¹ᵁ V k) le_rfl)) :
    IsQuasiRegularImmersion i
```

**`Stacks.AlgebraicGeometry.isQuasiRegularImmersion_iff_of_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularImmersion/OpenIndependence.lean, line 582](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularImmersion/OpenIndependence.lean#L582). The attribute's comment: “part (4): independence of the chosen open”.

> An immersion `i : Z ⟶ X` is quasi-regular if and only if, for one — equivalently any — open
> subscheme `U` of `X` through which `i` factors as a closed immersion `j : Z ⟶ U`, the defining
> ideal of `j` is a quasi-regular ideal sheaf on `U`.

```lean
theorem isQuasiRegularImmersion_iff_of_open {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i]
    (U : X.Opens) (j : Z ⟶ U.toScheme) [IsClosedImmersion j] (hij : j ≫ U.ι = i) :
    IsQuasiRegularImmersion i ↔
      IsQuasiRegularIdealSheaf U.toScheme.toLocallyRingedSpace.toRingedSpace
        (definingIdealOfHom j)
```

## Tag 063K, a lemma

[Tag 063K](https://stacks.math.columbia.edu/tag/063K) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isKoszulRegularImmersion_of_isRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/Implications.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/Implications.lean#L262).

> **A regular immersion is Koszul-regular.**  The first implication of Stacks tag 063K, between
> parts (1) and (2) of Stacks tag 063J.

```lean
theorem isKoszulRegularImmersion_of_isRegularImmersion (h : IsRegularImmersion i) :
    IsKoszulRegularImmersion i
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isH1RegularImmersion_of_isKoszulRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/Implications.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/Implications.lean#L270).

> **A Koszul-regular immersion is `H₁`-regular.**  The second implication of Stacks tag 063K,
> between parts (2) and (3) of Stacks tag 063J.

```lean
theorem isH1RegularImmersion_of_isKoszulRegularImmersion (h : IsKoszulRegularImmersion i) :
    IsH1RegularImmersion i
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isQuasiRegularImmersion_of_isH1RegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/Implications.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/Implications.lean#L277).

> **An `H₁`-regular immersion is quasi-regular.**  The third implication of Stacks tag 063K,
> between parts (3) and (4) of Stacks tag 063J.

```lean
theorem isQuasiRegularImmersion_of_isH1RegularImmersion (h : IsH1RegularImmersion i) :
    IsQuasiRegularImmersion i
```

## Tag 063L, a lemma

[Tag 063L](https://stacks.math.columbia.edu/tag/063L) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isRegularImmersion_iff_isKoszulRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/NoetherianRegularKoszul.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/NoetherianRegularKoszul.lean#L104). The attribute's comment: “regular iff Koszul-regular”.

> **Stacks tag 063L, parts (1) and (2).** An immersion into a locally Noetherian scheme is
> regular if and only if it is Koszul-regular.

```lean
theorem isRegularImmersion_iff_isKoszulRegularImmersion (i : Z ⟶ X) [IsImmersion i]
    [IsLocallyNoetherian X] :
    IsRegularImmersion i ↔ IsKoszulRegularImmersion i
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isKoszulRegularImmersion_iff_isH1RegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/NoetherianRegularKoszul.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/NoetherianRegularKoszul.lean#L131). The attribute's comment: “Koszul-regular iff H₁-regular”.

> **Stacks tag 063L, parts (2) and (3).** An immersion into a locally Noetherian scheme is
> Koszul-regular if and only if it is `H₁`-regular.

```lean
theorem isKoszulRegularImmersion_iff_isH1RegularImmersion (i : Z ⟶ X) [IsImmersion i]
    [IsLocallyNoetherian X] :
    IsKoszulRegularImmersion i ↔ IsH1RegularImmersion i
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isH1RegularImmersion_iff_isQuasiRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/NoetherianRegularKoszul.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/NoetherianRegularKoszul.lean#L141). The attribute's comment: “H₁-regular iff quasi-regular”.

> **Stacks tag 063L, parts (3) and (4).** An immersion into a locally Noetherian scheme is
> `H₁`-regular if and only if it is quasi-regular.

```lean
theorem isH1RegularImmersion_iff_isQuasiRegularImmersion (i : Z ⟶ X) [IsImmersion i]
    [IsLocallyNoetherian X] :
    IsH1RegularImmersion i ↔ IsQuasiRegularImmersion i
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.regularImmersion_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/NoetherianRegularKoszul.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/NoetherianRegularKoszul.lean#L153). The attribute's comment: “the four notions agree over a locally Noetherian base”. References: EGA IV (16.9.10); EGA IV (16.9.11), “more general”.

> **Stacks tag 063L.** For an immersion into a locally Noetherian scheme the four notions of
> regularity — regular, Koszul-regular, `H₁`-regular and quasi-regular — are equivalent.

```lean
theorem regularImmersion_tfae (i : Z ⟶ X) [IsImmersion i] [IsLocallyNoetherian X] :
    List.TFAE [IsRegularImmersion i, IsKoszulRegularImmersion i, IsH1RegularImmersion i,
      IsQuasiRegularImmersion i]
```

## Tag 067P, a lemma

[Tag 067P](https://stacks.math.columbia.edu/tag/067P) in the Stacks Project.

**`Stacks.AlgebraicGeometry.isRegularImmersion_pullback_snd_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularIdealSheaf/FlatBaseChange.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularIdealSheaf/FlatBaseChange.lean#L163). The attribute's comment: “regular”.

> A regular immersion remains a regular immersion after base change along a flat morphism.

```lean
theorem isRegularImmersion_pullback_snd_of_flat {Z X X' : Scheme.{u}} (i : Z ⟶ X) (g : X' ⟶ X)
    [IsImmersion i] [Flat g] (hi : IsRegularImmersion i) :
    IsRegularImmersion (pullback.snd i g)
```

**`Stacks.AlgebraicGeometry.isKoszulRegularImmersion_pullback_snd_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularIdealSheaf/FlatBaseChange.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularIdealSheaf/FlatBaseChange.lean#L221). The attribute's comment: “koszul”.

> A Koszul-regular immersion remains a Koszul-regular immersion after base change along a flat
> morphism.

```lean
theorem isKoszulRegularImmersion_pullback_snd_of_flat {Z X X' : Scheme.{u}} (i : Z ⟶ X)
    (g : X' ⟶ X) [IsImmersion i] [Flat g] (hi : IsKoszulRegularImmersion i) :
    IsKoszulRegularImmersion (pullback.snd i g)
```

**`Stacks.AlgebraicGeometry.isH1RegularImmersion_pullback_snd_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularIdealSheaf/FlatBaseChange.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularIdealSheaf/FlatBaseChange.lean#L275). The attribute's comment: “h1”.

> A `H₁`-regular immersion remains a `H₁`-regular immersion after base change along a flat
> morphism.

```lean
theorem isH1RegularImmersion_pullback_snd_of_flat {Z X X' : Scheme.{u}} (i : Z ⟶ X)
    (g : X' ⟶ X) [IsImmersion i] [Flat g] (hi : IsH1RegularImmersion i) :
    IsH1RegularImmersion (pullback.snd i g)
```

**`Stacks.AlgebraicGeometry.isQuasiRegularImmersion_pullback_snd_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularIdealSheaf/FlatBaseChange.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularIdealSheaf/FlatBaseChange.lean#L333). The attribute's comment: “quasi”. References: EGA IV (19.1.5), “(ii)”.

> A quasi-regular immersion remains a quasi-regular immersion after base change along a flat
> morphism.

```lean
theorem isQuasiRegularImmersion_pullback_snd_of_flat {Z X X' : Scheme.{u}} (i : Z ⟶ X)
    (g : X' ⟶ X) [IsImmersion i] [Flat g] (hi : IsQuasiRegularImmersion i) :
    IsQuasiRegularImmersion (pullback.snd i g)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isKoszulRegularIdealSheaf_pullbackIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/FlatBaseChange.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/FlatBaseChange.lean#L375). The attribute's comment: “part (2), ideal-sheaf level: the inverse image ideal sheaf `h⁻¹J·O_{X'}` of a Koszul-regular ideal sheaf along a morphism of locally ringed spaces with flat stalk maps is Koszul-regular”. References: SGA 6 VII (1.5), “flat base change, Koszul”.

> **Stacks tag 067P, part (2), at the level of ideal sheaves.** The inverse image ideal sheaf
> of a Koszul-regular ideal sheaf along a morphism with flat stalk maps is Koszul-regular.

```lean
theorem isKoszulRegularIdealSheaf_pullbackIdeal (hflat : HasFlatStalks h)
    (J : (structureSheafModule X.toRingedSpace).Submodule)
    (hJ : IsKoszulRegularIdealSheaf X.toRingedSpace J) :
    IsKoszulRegularIdealSheaf X'.toRingedSpace (pullbackIdeal h J)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isH1RegularIdealSheaf_pullbackIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/FlatBaseChange.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/FlatBaseChange.lean#L386). The attribute's comment: “part (3), ideal-sheaf level: the inverse image ideal sheaf `h⁻¹J·O_{X'}` of an H₁-regular ideal sheaf along a morphism of locally ringed spaces with flat stalk maps is H₁-regular”. References: SGA 6 VII (1.5), “flat base change, H1”.

> **Stacks tag 067P, part (3), at the level of ideal sheaves.** The inverse image ideal sheaf
> of an `H₁`-regular ideal sheaf along a morphism with flat stalk maps is `H₁`-regular.

```lean
theorem isH1RegularIdealSheaf_pullbackIdeal (hflat : HasFlatStalks h)
    (J : (structureSheafModule X.toRingedSpace).Submodule)
    (hJ : IsH1RegularIdealSheaf X.toRingedSpace J) :
    IsH1RegularIdealSheaf X'.toRingedSpace (pullbackIdeal h J)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isQuasiRegularIdealSheaf_pullbackIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/FlatBaseChange.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularIdealSheaf/FlatBaseChange.lean#L397). The attribute's comment: “part (4), ideal-sheaf level: the inverse image ideal sheaf `h⁻¹J·O_{X'}` of a quasi-regular ideal sheaf along a morphism of locally ringed spaces with flat stalk maps is quasi-regular”. References: SGA 6 VII (1.5), “flat base change, quasi”.

> **Stacks tag 067P, part (4), at the level of ideal sheaves.** The inverse image ideal sheaf
> of a quasi-regular ideal sheaf along a morphism with flat stalk maps is quasi-regular.

```lean
theorem isQuasiRegularIdealSheaf_pullbackIdeal (hflat : HasFlatStalks h)
    (J : (structureSheafModule X.toRingedSpace).Submodule)
    (hJ : IsQuasiRegularIdealSheaf X.toRingedSpace J) :
    IsQuasiRegularIdealSheaf X'.toRingedSpace (pullbackIdeal h J)
```

## Tag 063M, a lemma

[Tag 063M](https://stacks.math.columbia.edu/tag/063M) in the Stacks Project.

**`AlgebraicGeometry.isFiniteLocallyFree_universalConormalSheaf_of_isKoszulRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/UnramifiedConormal.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/UnramifiedConormal.lean#L97). The attribute's comment: “condition (2) for a Koszul-regular immersion, for the conormal sheaf of Tag 04F4. Condition (1) is at RegularImmersion/FinitePresentation.lean; condition (2) does not need Tag 063H, and is proved at RegularImmersion/ConormalLocallyFree.lean by a route through Tags 063G, 08RK, 01R3, 00NX and 05JM that never uses 063H”.

> The conormal sheaf of a Koszul-regular immersion of schemes, in the sense of Stacks 04F4, is
> finite locally free.

```lean
theorem isFiniteLocallyFree_universalConormalSheaf_of_isKoszulRegularImmersion
    {Z P : Scheme.{u}} (i : Z ⟶ P) [IsImmersion i] (hi : IsKoszulRegularImmersion i) :
    SheafOfModules.IsFiniteLocallyFree.{u, u, u} (universalConormalSheaf i)
```

**`Stacks.Conormal.isQuasiRegularImmersion_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularImmersion/ConormalQuasiRegularCriterion.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularImmersion/ConormalQuasiRegularCriterion.lean#L381). The attribute's comment: “the whole statement: an immersion is quasi-regular iff it is locally of finite presentation, its conormal sheaf is finite locally free, and the map of 0632 is an isomorphism”. References: EGA IV (16.9.8), “(i)”; EGA IV (17.12.1); EGA IV (19.1.3).

> An immersion `i : Z ⟶ X` of schemes is quasi-regular **if and only if** (1) it is locally of
> finite presentation, (2) its conormal sheaf `𝒞_{Z/X}` is finite locally free, and (3) the
> canonical map `Sym*(𝒞_{Z/X}) ⟶ 𝒞_{Z/X,*}` of [Stacks, Tag 0632] is an isomorphism in every
> degree.

```lean
theorem isQuasiRegularImmersion_iff (i : Z ⟶ X) [IsImmersion i] :
    Stacks.AlgebraicGeometry.RegularIdealSheaf.IsQuasiRegularImmersion i ↔
      LocallyOfFinitePresentation i ∧
        AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} (conormalSheaf i) ∧
          ∀ n : ℤ, IsIso ((conormalSymmetricHom i).app n)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.locallyOfFinitePresentation_of_isQuasiRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularImmersion/FinitePresentation.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularImmersion/FinitePresentation.lean#L103). The attribute's comment: “condition (1) of the statement, in the direction out of quasi-regularity: a quasi-regular immersion is locally of finite presentation. The whole iff is proved at Stacks.Conormal.isQuasiRegularImmersion_iff”. References: EGA IV (16.9.8), “(i), one direction”; EGA IV (16.9.9), “l.f.p. is necessary”; SGA 3 III (4.6.2), “more general”.

> **[Stacks, Tag 063M], condition (1) in the direction out of quasi-regularity.**  A
> quasi-regular immersion of schemes is locally of finite presentation.
>
> The canonical closed factor `i.liftCoborder` is locally of finite presentation by
> [Stacks, Tag 01TV], since the quasi-regular defining ideal sheaf is finitely generated over
> every affine open, and the remaining factor `i.coborderRange.ι` is an open immersion.

```lean
theorem locallyOfFinitePresentation_of_isQuasiRegularImmersion (i : Z ⟶ X) [IsImmersion i]
    (h : IsQuasiRegularImmersion i) : LocallyOfFinitePresentation i
```

## Tag 063N, a lemma

[Tag 063N](https://stacks.math.columbia.edu/tag/063N) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.mono_conormalLeftMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularImmersion/ConormalSequence.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularImmersion/ConormalSequence.lean#L400). The attribute's comment: “exactness at the left term: for an H₁-regular immersion `i` the canonical map `i^* 𝒞_{Y/X} ⟶ 𝒞_{Z/X}` is a monomorphism”.

> **[Stacks Project, Tag 063N]: the conormal sequence of an `H1`-regular immersion is exact at
> its left-hand term.** For immersions `Z --i--→ Y --j--→ X` with `i` an `H1`-regular immersion,
> the canonical map `i^* C_{Y/X} ⟶ C_{Z/X}` of [Stacks Project, Tag 01R4] is a monomorphism.

```lean
theorem mono_conormalLeftMap (i : Z ⟶ Y) (j : Y ⟶ X) [IsImmersion i] [IsImmersion j]
    (hi : IsH1RegularImmersion i) : Mono (conormalLeftMap i j)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.conormalSequence_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularImmersion/ConormalSequence.lean, line 554](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularImmersion/ConormalSequence.lean#L554). The attribute's comment: “exactness: the canonical sequence `0 ⟶ i^* 𝒞_{Y/X} ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y} ⟶ 0` of an H₁-regular immersion is short exact”.

> **[Stacks Project, Tag 063N]: the conormal sequence of an `H1`-regular immersion is short
> exact.** For immersions `Z --i--→ Y --j--→ X` with `i` an `H1`-regular immersion, the canonical
> sequence `0 ⟶ i^* C_{Y/X} ⟶ C_{Z/X} ⟶ C_{Z/Y} ⟶ 0` of [Stacks Project, Tag 062S] is a short
> exact sequence of `O_Z`-modules.
>
> Exactness in the middle and surjectivity on the right are [Stacks Project, Tag 062S]; what
> `H1`-regularity of `i` adds is injectivity on the left,
> `Stacks.AlgebraicGeometry.RegularIdealSheaf.mono_conormalLeftMap`.

```lean
theorem conormalSequence_shortExact (i : Z ⟶ Y) (j : Y ⟶ X) [IsImmersion i] [IsImmersion j]
    (hi : IsH1RegularImmersion i) : (conormalSequenceShortComplex i j).ShortExact
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.conormalSequence_locallySplit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularImmersion/ConormalSequence.lean, line 566](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularImmersion/ConormalSequence.lean#L566). The attribute's comment: “local splitness: on a neighbourhood of every point of `Z` the canonical sequence of an H₁-regular immersion splits”. References: EGA IV (16.9.13), “more general”; EGA IV (19.1.5), “more general”.

> **[Stacks Project, Tag 063N]: the conormal sequence of an `H1`-regular immersion is locally
> split.** Every point of `Z` has an open neighbourhood over which the short exact sequence
> `0 ⟶ i^* C_{Y/X} ⟶ C_{Z/X} ⟶ C_{Z/Y} ⟶ 0` splits, the restriction to an open being the slice
> restriction `SheafOfModules.over`.

```lean
theorem conormalSequence_locallySplit (i : Z ⟶ Y) (j : Y ⟶ X) [IsImmersion i] [IsImmersion j]
    (hi : IsH1RegularImmersion i) (z : Z) :
    ∃ V : Z.Opens, z ∈ V ∧ Nonempty (((conormalSequenceShortComplex i j).map
      (_root_.SheafOfModules.overFunctor
        (structureSheafRing Z.toLocallyRingedSpace.toRingedSpace) V)).Splitting)
```

## Tag 067Q, a lemma

[Tag 067Q](https://stacks.math.columbia.edu/tag/067Q) in the Stacks Project.

**`Stacks.AlgebraicGeometry.isRegularImmersion_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/Composition.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/Composition.lean#L155). The attribute's comment: “composition_regular”. References: EGA IV (19.1.5); SGA 6 VIII (1.1), “special case”.

> The composite of two regular immersions of schemes is a regular immersion.

```lean
theorem isRegularImmersion_comp {Z Y X : Scheme.{u}} (i : Z ⟶ Y) (j : Y ⟶ X) [IsImmersion i]
    [IsImmersion j] (hi : IsRegularImmersion i) (hj : IsRegularImmersion j) :
    IsRegularImmersion (i ≫ j)
```

**`Stacks.AlgebraicGeometry.isKoszulRegularImmersion_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionComposition.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionComposition.lean#L263). The attribute's comment: “composition_koszul_regular”. References: SGA 6 VII (1.7); SGA 6 VIII (1.1); SGA 6 VIII (1.3).

> **Stacks tag 067Q, the Koszul-regular case.**  The composite of two Koszul-regular immersions
> of schemes is a Koszul-regular immersion.

```lean
theorem isKoszulRegularImmersion_comp {Z Y X : Scheme.{u}} (i : Z ⟶ Y) (j : Y ⟶ X)
    [IsImmersion i] [IsImmersion j] (hi : IsKoszulRegularImmersion i)
    (hj : IsKoszulRegularImmersion j) :
    IsKoszulRegularImmersion (i ≫ j)
```

**`Stacks.AlgebraicGeometry.isH1RegularImmersion_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionComposition.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionComposition.lean#L282). The attribute's comment: “composition_h1_regular”.

> **Stacks tag 067Q, the `H₁`-regular case.**  The composite of two `H₁`-regular immersions of
> schemes is an `H₁`-regular immersion.

```lean
theorem isH1RegularImmersion_comp {Z Y X : Scheme.{u}} (i : Z ⟶ Y) (j : Y ⟶ X) [IsImmersion i]
    [IsImmersion j] (hi : IsH1RegularImmersion i) (hj : IsH1RegularImmersion j) :
    IsH1RegularImmersion (i ≫ j)
```

**`Stacks.AlgebraicGeometry.isQuasiRegularImmersion_comp_of_isH1RegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionComposition.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionComposition.lean#L300). The attribute's comment: “composition_h1_quasi_regular”.

> **Stacks tag 067Q, the mixed case.**  The composite of an `H₁`-regular immersion of schemes
> and a quasi-regular immersion of schemes is a quasi-regular immersion.

```lean
theorem isQuasiRegularImmersion_comp_of_isH1RegularImmersion {Z Y X : Scheme.{u}} (i : Z ⟶ Y)
    (j : Y ⟶ X) [IsImmersion i] [IsImmersion j] (hi : IsH1RegularImmersion i)
    (hj : IsQuasiRegularImmersion j) :
    IsQuasiRegularImmersion (i ≫ j)
```

## Tag 068Z, a lemma

[Tag 068Z](https://stacks.math.columbia.edu/tag/068Z) in the Stacks Project.

**`Stacks.AlgebraicGeometry.isH1RegularImmersion_of_comp_of_isSplitExactConormalSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SplitConormalH1Regular.lean, line 427](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SplitConormalH1Regular.lean#L427). The attribute's comment: “(2) H₁-regularity descends to the first immersion”.

> **[Stacks Project, Tag 068Z], part (2).** For immersions `i : Z ⟶ Y` and `j : Y ⟶ X` with `j`
> locally of finite presentation whose conormal sequence is exact and locally split,
> `H₁`-regularity of `i ≫ j` descends to `i`.

```lean
theorem isH1RegularImmersion_of_comp_of_isSplitExactConormalSequence
    (i : Z ⟶ Y) (j : Y ⟶ X) [IsImmersion i] [IsImmersion j] [LocallyOfFinitePresentation j]
    (hS : IsSplitExactConormalSequence i j) (hij : IsH1RegularImmersion (i ≫ j)) :
    IsH1RegularImmersion i
```

**`Stacks.AlgebraicGeometry.isKoszulRegularImmersion_of_comp_of_isSplitExactConormalSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SplitConormalKoszulRegular.lean, line 473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SplitConormalKoszulRegular.lean#L473). The attribute's comment: “(3) Koszul-regularity of the first immersion”.

> **[Stacks Project, Tag 068Z], part (3).** For immersions `i : Z ⟶ Y` and `j : Y ⟶ X` with `j`
> locally of finite presentation whose conormal sequence is exact and locally split, `i` is
> Koszul-regular as soon as both `j` and `i ≫ j` are.

```lean
theorem isKoszulRegularImmersion_of_comp_of_isSplitExactConormalSequence
    (i : Z ⟶ Y) (j : Y ⟶ X) [IsImmersion i] [IsImmersion j] [LocallyOfFinitePresentation j]
    (hS : IsSplitExactConormalSequence i j) (hj : IsKoszulRegularImmersion j)
    (hij : IsKoszulRegularImmersion (i ≫ j)) :
    IsKoszulRegularImmersion i
```

**`Stacks.AlgebraicGeometry.isQuasiRegularImmersion_of_comp_of_isSplitExactConormalSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SplitConormalQuasiRegular.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/SplitConormalQuasiRegular.lean#L454). The attribute's comment: “(1) quasi-regularity descends to the first immersion”.

> **[Stacks Project, Tag 068Z], part (1).** For immersions `i : Z ⟶ Y` and `j : Y ⟶ X` with `j`
> locally of finite presentation whose conormal sequence is exact and locally split,
> quasi-regularity of `i ≫ j` descends to `i`.

```lean
theorem isQuasiRegularImmersion_of_comp_of_isSplitExactConormalSequence
    (i : Z ⟶ Y) (j : Y ⟶ X) [IsImmersion i] [IsImmersion j] [LocallyOfFinitePresentation j]
    (hS : IsSplitExactConormalSequence i j) (hij : IsQuasiRegularImmersion (i ≫ j)) :
    IsQuasiRegularImmersion i
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isKoszulRegularIdealSheaf_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularImmersion/ConormalPermanence.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularImmersion/ConormalPermanence.lean#L412). The attribute's comment: “part (3) for closed immersions: Koszul-regularity of `j` and of `i ≫ j` together with injectivity of the cotangent-fibre map `I_x/𝔪_x I_x ⟶ J_x/𝔪_x J_x` gives Koszul-regularity of `i`. That injectivity is a hypothesis here, not derived from exactness and local splitness of the conormal sequence”.

> **[Stacks Project, Tag 068Z] part (3) for closed immersions, from injectivity on cotangent
> fibres.** Let `Z --i--→ Y --j--→ X` be closed immersions with Koszul-regular defining ideal
> sheaves for `j` and for `i ≫ j`.  If at every point of `Z` the induced map of cotangent fibres
> `I_x/𝔪_x I_x → J_x/𝔪_x J_x` of the two defining ideals is injective, then the defining ideal
> sheaf of `i` is Koszul-regular.
>
> Over an affine open `U` of `X` around the image of the point, local generators `f` of the ideal
> of `Y` extend to local generators `f, g` of the ideal of `Z`, both Koszul-regular, and the
> images of the `g` under `j` on sections generate the ideal of `Z` in `Y` and are Koszul-regular
> by [Stacks Project, Tag 068M].

```lean
theorem isKoszulRegularIdealSheaf_of_comp (i : Z ⟶ Y) (j : Y ⟶ X)
    [IsClosedImmersion i] [IsClosedImmersion j]
    (hinj : ∀ z : Z, Function.Injective (conormalFibreMap i j z))
    (hj : IsKoszulRegularIdealSheaf X.toRingedSpace (definingIdealOfHom j))
    (hij : IsKoszulRegularIdealSheaf X.toRingedSpace (definingIdealOfHom (i ≫ j))) :
    IsKoszulRegularIdealSheaf Y.toRingedSpace (definingIdealOfHom i)
```

## Tag 0690, a lemma

[Tag 0690](https://stacks.math.columbia.edu/tag/0690) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.exists_opens_isSplitExactConormalSequence_of_split`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/H1RegularSplitConormal.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/H1RegularSplitConormal.lean#L146). The attribute's comment: “(2) => (3)”. References: EGA IV (19.1.5), “(iv)”; SGA 6 VII (4.2), “partial”.

> **Stacks tag 0690, `(2) ⇒ (3)`.**  Let `i : Z ⟶ Y` and `j : Y ⟶ X` be immersions of schemes
> and let `z : Z`.  If `i` and `i ≫ j` are regular immersions in a neighbourhood of `z`, then
> `i ≫ j` is a regular immersion in a neighbourhood of `z` and the conormal sequence
> `0 ⟶ i^* 𝒞_{Y/X} ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y} ⟶ 0` is exact and locally split in a neighbourhood
> of `z`.

```lean
theorem exists_opens_isSplitExactConormalSequence_of_split (i : Z ⟶ Y) (j : Y ⟶ X)
    [IsImmersion i] [IsImmersion j] (z : Z)
    (hi : ∃ W : Z.Opens, z ∈ W ∧ IsRegularImmersion (W.ι ≫ i))
    (hji : ∃ U : Z.Opens, z ∈ U ∧ IsRegularImmersion (U.ι ≫ (i ≫ j))) :
    (∃ U : Z.Opens, z ∈ U ∧ IsRegularImmersion (U.ι ≫ (i ≫ j))) ∧
      ∃ W : Z.Opens, z ∈ W ∧ IsSplitExactConormalSequence (W.ι ≫ i) j
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.exists_opens_isRegularImmersion_of_factors_of_split`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/H1RegularSplitConormal.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/H1RegularSplitConormal.lean#L172). The attribute's comment: “(2) => (1)”.

> **Stacks tag 0690, `(2) ⇒ (1)`.**  Let `i : Z ⟶ Y` and `j : Y ⟶ X` be immersions of schemes
> with `X` locally Noetherian and let `z : Z`.  If `i` and `i ≫ j` are regular immersions in a
> neighbourhood of `z`, then `i` is a regular immersion in a neighbourhood of `z` and `j` is one in
> a neighbourhood of `i z`.

```lean
theorem exists_opens_isRegularImmersion_of_factors_of_split (i : Z ⟶ Y) (j : Y ⟶ X)
    [IsImmersion i] [IsImmersion j] [IsLocallyNoetherian X] (z : Z)
    (hi : ∃ W : Z.Opens, z ∈ W ∧ IsRegularImmersion (W.ι ≫ i))
    (hji : ∃ U : Z.Opens, z ∈ U ∧ IsRegularImmersion (U.ι ≫ (i ≫ j))) :
    (∃ W : Z.Opens, z ∈ W ∧ IsRegularImmersion (W.ι ≫ i)) ∧
      ∃ V : Y.Opens, i.base z ∈ V ∧ IsRegularImmersion (V.ι ≫ j)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.exists_opens_isSplitExactConormalSequence_of_factors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/H1RegularSplitConormal.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/H1RegularSplitConormal.lean#L201). The attribute's comment: “(1) => (3)”. References: EGA IV (19.1.5), “partial”; SGA 6 VII (4.2), “partial”; SGA 6 VIII (1.3), “clause (i), special case”.

> **Stacks tag 0690, `(1) ⇒ (3)`.**  Let `i : Z ⟶ Y` and `j : Y ⟶ X` be immersions of schemes
> with `X` locally Noetherian and let `z : Z`.  If `i` is a regular immersion in a neighbourhood of
> `z` and `j` is one in a neighbourhood of `i z`, then `i ≫ j` is a regular immersion in a
> neighbourhood of `z` and the conormal sequence of the pair is exact and locally split in a
> neighbourhood of `z`.

```lean
theorem exists_opens_isSplitExactConormalSequence_of_factors (i : Z ⟶ Y) (j : Y ⟶ X)
    [IsImmersion i] [IsImmersion j] [IsLocallyNoetherian X] (z : Z)
    (hi : ∃ W : Z.Opens, z ∈ W ∧ IsRegularImmersion (W.ι ≫ i))
    (hj : ∃ V : Y.Opens, i.base z ∈ V ∧ IsRegularImmersion (V.ι ≫ j)) :
    (∃ U : Z.Opens, z ∈ U ∧ IsRegularImmersion (U.ι ≫ (i ≫ j))) ∧
      ∃ W : Z.Opens, z ∈ W ∧ IsSplitExactConormalSequence (W.ι ≫ i) j
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.tfae_isRegularImmersion_near`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/H1RegularSplitConormal.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/H1RegularSplitConormal.lean#L215).

> **Stacks tag 0690.**  For immersions `i : Z ⟶ Y` and `j : Y ⟶ X` with `X` locally Noetherian
> and `z : Z`, the following are equivalent: (1) `i` is a regular immersion near `z` and `j` is one
> near `i z`; (2) `i` and `i ≫ j` are regular immersions near `z`; (3) `i ≫ j` is a regular
> immersion near `z` and the conormal sequence of the pair is exact and locally split near `z`.

```lean
theorem tfae_isRegularImmersion_near (i : Z ⟶ Y) (j : Y ⟶ X) [IsImmersion i] [IsImmersion j]
    [IsLocallyNoetherian X] (z : Z) :
    List.TFAE
      [(∃ W : Z.Opens, z ∈ W ∧ IsRegularImmersion (W.ι ≫ i)) ∧
          ∃ V : Y.Opens, i.base z ∈ V ∧ IsRegularImmersion (V.ι ≫ j),
        (∃ W : Z.Opens, z ∈ W ∧ IsRegularImmersion (W.ι ≫ i)) ∧
          ∃ U : Z.Opens, z ∈ U ∧ IsRegularImmersion (U.ι ≫ (i ≫ j)),
        (∃ U : Z.Opens, z ∈ U ∧ IsRegularImmersion (U.ι ≫ (i ≫ j))) ∧
          ∃ W : Z.Opens, z ∈ W ∧ IsSplitExactConormalSequence (W.ι ≫ i) j]
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.exists_opens_isRegularImmersion_of_split_near`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/NoetherianSplitConormal.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/NoetherianSplitConormal.lean#L199). The attribute's comment: “(3) => (1)”.

> **Stacks tag 0690, `(3) ⇒ (1)`.**  Let `i : Z ⟶ Y` and `j : Y ⟶ X` be immersions of schemes
> with `X` locally Noetherian, let `z : Z` and let `y = i z`.  If `i ≫ j` is a regular immersion in
> a neighbourhood of `z` and the conormal sequence of the pair is exact and locally split in a
> neighbourhood of `z`, then `i` is a regular immersion in a neighbourhood of `z` and `j` is one in
> a neighbourhood of `y`.

```lean
theorem exists_opens_isRegularImmersion_of_split_near (i : Z ⟶ Y) (j : Y ⟶ X) [IsImmersion i]
    [IsImmersion j] [IsLocallyNoetherian X] (z : Z)
    (hji : ∃ U : Z.Opens, z ∈ U ∧ IsRegularImmersion (U.ι ≫ (i ≫ j)))
    (hS : ∃ W : Z.Opens, z ∈ W ∧ IsSplitExactConormalSequence (W.ι ≫ i) j) :
    (∃ W : Z.Opens, z ∈ W ∧ IsRegularImmersion (W.ι ≫ i)) ∧
      ∃ V : Y.Opens, i.base z ∈ V ∧ IsRegularImmersion (V.ι ≫ j)
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.exists_opens_isRegularImmersion_comp_of_factors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/NoetherianSplitConormal.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/NoetherianSplitConormal.lean#L263). The attribute's comment: “(1) => (2)”.

> **Stacks tag 0690, `(1) ⇒ (2)`.**  Let `i : Z ⟶ Y` and `j : Y ⟶ X` be immersions of schemes
> with `X` locally Noetherian and let `z : Z`.  If `i` is a regular immersion in a neighbourhood of
> `z` and `j` is one in a neighbourhood of `i z`, then `i ≫ j` is a regular immersion in a
> neighbourhood of `z`.

```lean
theorem exists_opens_isRegularImmersion_comp_of_factors (i : Z ⟶ Y) (j : Y ⟶ X) [IsImmersion i]
    [IsImmersion j] [IsLocallyNoetherian X] (z : Z)
    (hi : ∃ W : Z.Opens, z ∈ W ∧ IsRegularImmersion (W.ι ≫ i))
    (hj : ∃ V : Y.Opens, i.base z ∈ V ∧ IsRegularImmersion (V.ι ≫ j)) :
    ∃ U : Z.Opens, z ∈ U ∧ IsRegularImmersion (U.ι ≫ (i ≫ j))
```

## Tag 0691, a remark

[Tag 0691](https://stacks.math.columbia.edu/tag/0691) in the Stacks Project.

**`Stacks.Examples.regular_immersion_not_permanent_in_middle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Scheme/RegularImmersionNotPermanentInMiddle.lean, line 710](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Scheme/RegularImmersionNotPermanentInMiddle.lean#L710). The attribute's comment: “The counterexample of the remark for `X = 𝐀¹_k`, `Y = Spec(k[x]/(x²))` and `Z = Spec(k[x]/(x))` over an arbitrary field `k`, at the level of schemes throughout. The three immersions are the `Spec` of the quotient maps `k[x] → k[x]/(x²)` (that is `j`), `k[x] → k[x]/(x)` (that is `j ∘ i`, identified with the composite by `Stacks.Examples.simpleOriginImmersion_comp_doubleOriginLineImmersion`) and `k[x]/(x²) → k[x]/(x)` (that is `i`). The predicate is `Stacks.AlgebraicGeometry.RegularIdealSheaf.IsRegularImmersion`, part (1) of Stacks tag 063J and the one whose variants the statements carrying Stacks tag 0690 compare; the `in a neighbourhood of a point` form in which Stacks tag 0690 states its three parts is `Stacks.Examples.IsRegularImmersionAt`, and the splitting condition of its part (3) is `Stacks.AlgebraicGeometry.IsSplitExactConormalSequence` on a neighbourhood, the form in which the proved implications of Stacks tag 0690 state it. Both forms are delivered: regularity of `j` at every point of `Y`, of `i ≫ j` at every point of `Z` and of both globally, against the refutation of regularity of `i` at every point of `Z` and globally. All three parts of Stacks tag 0690 are refuted, each as a whole and at every point of `Z`: parts (1) and (2) through their common first half, part (3) through its second half, the splitting, since its first half holds here. That last refutation runs through the implication `(3) ⇒ (1)` of Stacks tag 0690, `Stacks.AlgebraicGeometry.RegularIdealSheaf.exists_opens_isRegularImmersion_of_split_near`, which is proved; nothing here rests on an unproved result. The three ideal-level statements are retained as the affine half to which that predicate reduces by Stacks tag 063G. No hypothesis is carried beyond `k` being a field.”.

> **Stacks tag 0691.** Regularity of an immersion is not inherited by the middle term of a
> factorization. For `Z = Spec(k[x]/(x)) --i--→ Y = Spec(k[x]/(x²)) --j--→ X = 𝐀¹_k = Spec(k[x])`
> the two outer immersions `j` and `j ∘ i` are regular immersions — at every point of their sources
> and globally — while the middle one, `i`, is a regular immersion in no neighbourhood of any point
> of `Z` and in particular not globally, and the conormal sequence of the pair is exact and split in
> no neighbourhood of any point of `Z`; at the level of ideals, the ideals of `Y` in `X` and of `Z`
> in `X` are each generated by a weakly regular sequence and the ideal of `Z` in `Y` is generated by
> none. So each of the three parts of Stacks tag 0690 fails at every point of `Z` — parts (1) and
> (2) through their common first half, regularity of `i` near the point, and part (3) through its
> second half, the splitting, its first half being true — while "`j ∘ i` and `j` are regular
> immersions at `z` and `y`" holds, which is the content of the remark.

```lean
theorem regular_immersion_not_permanent_in_middle (k : Type*) [Field k] :
    -- `j` is a regular immersion at every point of `Y`, and `j ∘ i` at every point of `Z`
    (∀ y, IsRegularImmersionAt (doubleOriginLineImmersion k) y) ∧
      (∀ z, IsRegularImmersionAt
        (simpleOriginImmersion k ≫ doubleOriginLineImmersion k) z) ∧
      -- while `i` is a regular immersion in no neighbourhood of any point of `Z`
      (∀ z, ¬ IsRegularImmersionAt (simpleOriginImmersion k) z) ∧
      -- and the conormal sequence is exact and split in no neighbourhood of any point of `Z`
      (∀ z, ¬ ∃ W : (Spec (CommRingCat.of (SimpleOriginRing k))).Opens, z ∈ W ∧
        IsSplitExactConormalSequence (W.ι ≫ simpleOriginImmersion k)
          (doubleOriginLineImmersion k)) ∧
      -- so that each of the three parts of Stacks tag 0690 fails at every point of `Z`
      (∀ z, ¬ (IsRegularImmersionAt (simpleOriginImmersion k) z ∧
        IsRegularImmersionAt (doubleOriginLineImmersion k) ((simpleOriginImmersion k).base z))) ∧
      (∀ z, ¬ (IsRegularImmersionAt (simpleOriginImmersion k) z ∧
        IsRegularImmersionAt (simpleOriginImmersion k ≫ doubleOriginLineImmersion k) z)) ∧
      (∀ z, ¬ (IsRegularImmersionAt (simpleOriginImmersion k ≫ doubleOriginLineImmersion k) z ∧
        ∃ W : (Spec (CommRingCat.of (SimpleOriginRing k))).Opens, z ∈ W ∧
          IsSplitExactConormalSequence (W.ι ≫ simpleOriginImmersion k)
            (doubleOriginLineImmersion k))) ∧
      -- the same three facts globally
      RegularIdealSheaf.IsRegularImmersion (doubleOriginLineImmersion k) ∧
      RegularIdealSheaf.IsRegularImmersion
        (simpleOriginImmersion k ≫ doubleOriginLineImmersion k) ∧
      ¬ RegularIdealSheaf.IsRegularImmersion (simpleOriginImmersion k) ∧
      -- and at the level of ideals, to which Stacks tag 063G reduces them
      (∃ rs : List (Polynomial k),
        Ideal.ofList rs = doubleOriginIdeal k ∧ IsWeaklyRegular (Polynomial k) rs) ∧
      (∃ rs : List (Polynomial k),
        Ideal.ofList rs = simpleOriginIdeal k ∧ IsWeaklyRegular (Polynomial k) rs) ∧
      (¬ ∃ rs : List (DoubleOriginRing k),
        Ideal.ofList rs = doubleOriginPointIdeal k ∧
          IsWeaklyRegular (DoubleOriginRing k) rs)
```

## Tag 0692, a lemma

[Tag 0692](https://stacks.math.columbia.edu/tag/0692) in the Stacks Project.

**`Stacks.AlgebraicGeometry.exists_smooth_surjective_regular_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/KoszulRegularSmoothCover.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/KoszulRegularSmoothCover.lean#L493).

> **Stacks Project, Tag 0692.**  A Koszul-regular closed immersion becomes a regular immersion
> after a surjective smooth base change of its target.
>
> Both conditions are stated with the classes of Stacks tag 063J, parts (2) and (1):
> `RegularIdealSheaf.IsKoszulRegularImmersion` and `RegularIdealSheaf.IsRegularImmersion`.

```lean
theorem exists_smooth_surjective_regular_baseChange {Z X : Scheme.{u}} (i : Z ⟶ X)
    [IsClosedImmersion i] (hi : RegularIdealSheaf.IsKoszulRegularImmersion i) :
    ∃ (X' : Scheme.{u}) (g : X' ⟶ X),
      Surjective g ∧ Smooth g ∧
        RegularIdealSheaf.IsRegularImmersion (pullback.snd i g)
```

## Tag 0E9J, a lemma

[Tag 0E9J](https://stacks.math.columbia.edu/tag/0E9J) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isRegularImmersion_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/ImmersionOfRegularSchemes.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/ImmersionOfRegularSchemes.lean#L65). References: EGA IV (19.7.5), “more general”.

> **Stacks tag 0E9J.** An immersion between regular schemes is a regular immersion.

```lean
theorem isRegularImmersion_of_isRegular {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i]
    (hZ : AlgebraicGeometry.IsRegular Z) (hX : AlgebraicGeometry.IsRegular X) :
    IsRegularImmersion i
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.22, Tag 0638](https://stacks.math.columbia.edu/tag/0638)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
