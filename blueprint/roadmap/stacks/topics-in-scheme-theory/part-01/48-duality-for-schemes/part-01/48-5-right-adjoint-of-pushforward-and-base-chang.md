---
declaration: section
origin: cited
lean: Stacks.Duality.twistedInverseImageBaseChangeMap, Stacks.Duality.torIndependentTwistedInverseImageBaseChange, Stacks.Duality.torIndependentTwistedInverseImageBaseChange_homEquiv, Stacks.Duality.twistedInverseImageBaseChangeMap_vcomp, Stacks.Duality.twistedInverseImageBaseChangeMap_paste_vert_app, Stacks.Duality.twistedInverseImageBaseChangeMap_hcomp, Stacks.Duality.twistedInverseImageBaseChangeMap_paste_horiz_app, Stacks.Duality.twistedInverseImageBaseChangeMap_grid_app
statement: formalized
proof: formalized
---

# 48.5 Right adjoint of pushforward and base change, I

Section 48.5 of the Stacks Project, [Tag 0AA5](https://stacks.math.columbia.edu/tag/0AA5). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AA6, an equation

[Tag 0AA6](https://stacks.math.columbia.edu/tag/0AA6) in the Stacks Project.

**`Stacks.Duality.twistedInverseImageBaseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BaseChange.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BaseChange.lean#L223). The attribute's comment: “variant: the composite for any cartesian square at which ξ is invertible; the tag is Stacks.Duality.torIndependentTwistedInverseImageBaseChange”.

> **The base change map `L(g')^* ∘ a ⟶ a' ∘ Lg^*`** of [Stacks, Tag 0AA6], Equation 48.5.0.1,
> for a cartesian square of schemes: the unit of `Lg^* ⊣ Rg_*`, then the inverse of
> `L(g')^* ⋆ ξ ⋆ Lg^*`, then the counit of `L(g')^* ⊣ Rg'_*`.
>
> Invertibility of `ξ` is an instance argument; for a Tor-independent square of quasi-compact
> quasi-separated schemes it is [Stacks, Tag 0A9K], and the map at those hypotheses is
> `Stacks.Duality.torIndependentTwistedInverseImageBaseChange`.

```lean
def twistedInverseImageBaseChangeMap (sq : IsPullback g' f' f g)
    [IsIso (twistedInverseImagePushforwardBaseChange g' f' f g hpushg' hpushf hpushf' hpushg
      sq)] :
    twistedInverseImage f hpushf ⋙ quasiCoherentDerivedPullback' g' ⟶
      quasiCoherentDerivedPullback' g ⋙ twistedInverseImage f' hpushf'
```

**`Stacks.Duality.torIndependentTwistedInverseImageBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/TorIndependentBaseChangeMap.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/TorIndependentBaseChangeMap.lean#L70).

> **The base change map `L(g')^* ∘ a ⟶ a' ∘ Lg^*` of [Stacks, Tag 0AA6]**, Equation 48.5.0.1,
> for a cartesian square of quasi-compact and quasi-separated schemes with `f` and `g` Tor
> independent: the unit of `Lg^* ⊣ Rg_*`, then the inverse of `L(g')^* ⋆ ξ ⋆ Lg^*`, which exists by
> [Stacks, Tag 0A9K], then the counit of `L(g')^* ⊣ Rg'_*`.

```lean
def torIndependentTwistedInverseImageBaseChange (sq : IsPullback g' f' f g)
    (hTor : TorIndependent f g) :
    twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f) ⋙
        quasiCoherentDerivedPullback' g' ⟶
      quasiCoherentDerivedPullback' g ⋙
        twistedInverseImage f' (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
```

**`Stacks.Duality.torIndependentTwistedInverseImageBaseChange_homEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/TorIndependentBaseChangeMap.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/TorIndependentBaseChangeMap.lean#L88). The attribute's comment: “the adjoint form a ⟶ a ∘ Rg_* ∘ Lg^* ⟵ Rg'_* ∘ a' ∘ Lg^*”.

> **The adjoint form of the base change map of [Stacks, Tag 0AA6].** Under
> `L(g')^* ⊣ Rg'_*` the component at `K` of `L(g')^* ∘ a ⟶ a' ∘ Lg^*` corresponds to
> `a(K) ⟶ a(Rg_* Lg^* K) ⟵ Rg'_* a'(Lg^* K)`, the image under `a` of the unit of `Lg^* ⊣ Rg_*`
> followed by the inverse of `ξ : Rg'_* ∘ a' ⟶ a ∘ Rg_*`.

```lean
theorem torIndependentTwistedInverseImageBaseChange_homEquiv (sq : IsPullback g' f' f g)
    (hTor : TorIndependent f g) (K : quasiCoherentDerivedCategory Y) :
    haveI := isIso_twistedInverseImagePushforwardBaseChange_of_torIndependent sq hTor
    (quasiCoherentDerivedAdjunction g' (isQuasicoherent_homology_derivedPullback' g')
        (isQuasicoherent_homology_derivedPushforward_of_qcqs g')).homEquiv _ _
        ((torIndependentTwistedInverseImageBaseChange sq hTor).app K) =
      (twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).map
          ((quasiCoherentDerivedAdjunction g (isQuasicoherent_homology_derivedPullback' g)
            (isQuasicoherent_homology_derivedPushforward_of_qcqs g)).unit.app K) ≫
        (inv (twistedInverseImagePushforwardBaseChange g' f' f g
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g) sq)).app
            ((quasiCoherentDerivedPullback' g).obj K)
```

## Tag 0ATQ, a lemma

[Tag 0ATQ](https://stacks.math.columbia.edu/tag/0ATQ) in the Stacks Project.

**`Stacks.Duality.twistedInverseImageBaseChangeMap_vcomp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BaseChangeStackingMate.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BaseChangeStackingMate.lean#L380). The attribute's comment: “for the base change map of Stacks 0AA6 attached to the twisted inverse image f^x of Stacks 0A9E -- the right adjoint of Rf_* on D_QCoh -- and for the comparison (f then g)^x = g^x then f^x of Stacks 0ATX: the map of the outer rectangle of a vertical stack of two cartesian squares is the horizontal composite of the maps of the two squares, read through those comparisons. The source's quasi-compactness and quasi-separatedness enter as the preservation of quasi-coherent cohomology by derived direct and inverse image along the morphisms of the diagram and as the existence of the six right adjoints, which is what Stacks 08D5 part (1) and Stacks 0A9E produce for a quasi-compact quasi-separated morphism; Stacks.Duality.twistedInverseImageCompIsoOfQcqs is the pattern that discharges them. Invertibility of the transformation xi of Stacks 0A9K for each of the two squares is an instance argument, exactly as in Stacks.Duality.twistedInverseImageBaseChangeMap where the base change map is defined, and it is Stacks 0A9K that produces it for a Tor-independent square. What is NOT claimed is the passage from f^x to the f^! of a general compactification, Stacks.Duality.upperShriek, which needs the independence of the chosen compactification, Stacks 0AA0”.

> **[Stacks, Tag 0ATQ] (Lemma 48.5.1): the base change maps of a vertical stack of two
> cartesian squares compose to the base change map of the outer rectangle.** For
>
> ```
> X' --k--> X
> |f'       |f
> Y' --l--> Y
> |g'       |g
> Z' --m--> Z
> ```
>
> with both squares cartesian, the base change map `Stacks.Duality.twistedInverseImageBaseChangeMap`
> of [Stacks, Tag 0AA6] for the rectangle — the square with horizontal edges `k` and `m` and
> vertical edges `f' ≫ g'` and `f ≫ g` — is the horizontal composite of the base change maps of the
> lower and of the upper square, the twisted inverse images along the two composite verticals being
> read through the comparison `Stacks.Duality.twistedInverseImageCompIso` of [Stacks, Tag 0ATX].
>
> The source's proof reduces the statement to the identity `ξ_rect = ξ_bot ≫ₕ ξ_top`, which is
> `Stacks.Duality.twistedInverseImagePushforwardBaseChange_vcomp`; the passage from that identity to
> this one is the compatibility of `CategoryTheory.mateEquiv` with vertical composition, because
> each base change map is the mate of the inverse of the corresponding `ξ`
> (`Stacks.Duality.twistedInverseImageBaseChangeMap_eq_mateEquiv_symm`).

```lean
theorem twistedInverseImageBaseChangeMap_vcomp (sq₁ : IsPullback k f' f l)
    (sq₂ : IsPullback l g' g m)
    [IsIso (twistedInverseImagePushforwardBaseChange k f' f l hpushk hpushf hpushf' hpushl sq₁)]
    [IsIso (twistedInverseImagePushforwardBaseChange l g' g m hpushl hpushg hpushg' hpushm sq₂)] :
    letI := isIso_twistedInverseImagePushforwardBaseChange_vcomp k f' f l g' g m hpushk hpushf
      hpushf' hpushl hpushg hpushg' hpushm hpushfg hpushf'g' sq₁ sq₂
    twistedInverseImageBaseChangeMap k (f' ≫ g') (f ≫ g) m hpushk hpushfg hpushf'g' hpushm
        (sq₁.paste_vert sq₂) =
      ((TwoSquare.mk _ _ _ _ (twistedInverseImageBaseChangeMap l g' g m hpushl hpushg hpushg'
              hpushm sq₂) ≫ₕ
          TwoSquare.mk _ _ _ _ (twistedInverseImageBaseChangeMap k f' f l hpushk hpushf hpushf'
            hpushl sq₁)).whiskerTop
        (twistedInverseImageCompIso f g hpushf hpushg hpushfg).hom).whiskerBottom
        (twistedInverseImageCompIso f' g' hpushf' hpushg' hpushf'g').inv
```

**`Stacks.Duality.twistedInverseImageBaseChangeMap_paste_vert_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/TorIndependentBaseChangePasteVert.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/TorIndependentBaseChangePasteVert.lean#L175).

> **[Stacks, Tag 0ATQ].** Consider a commutative diagram
> ```
> X' --k--> X
> |         |
> f'        f
> v         v
> Y' --l--> Y
> |         |
> g'        g
> v         v
> Z' --m--> Z
> ```
> of quasi-compact and quasi-separated schemes in which both squares are cartesian, `f` and `l`
> are Tor independent and `g` and `m` are Tor independent. Then the base change maps
> (Equation 48.5.0.1 of [Stacks, Tag 0AA6]) of the two squares compose to the base change map of
> the outer rectangle: with `a`, `b`, `c` the right adjoints of `Rf_*`, `Rg_*`, `R(f ≫ g)_*` and
> `a'`, `b'`, `c'` those of `Rf'_*`, `Rg'_*`, `R(f' ≫ g')_*`, for every `K ∈ D_QCoh(𝒪_Z)` the map
> `Lk^* c(K) ⟶ c'(Lm^* K)` of the rectangle is
>
> ```
> Lk^* c(K) = Lk^* a(b(K)) ⟶ a'(Ll^* b(K)) ⟶ a'(b'(Lm^* K)) = c'(Lm^* K),
> ```
>
> the identifications `c = b ⋙ a` and `c' = b' ⋙ a'` being those of [Stacks, Tag 0ATX]
> (`Stacks.Duality.twistedInverseImageCompIso`). The base change map of the rectangle is defined
> because its `ξ` is invertible,
> `Stacks.Duality.isIso_twistedInverseImagePushforwardBaseChange_of_paste_vert`.

```lean
theorem twistedInverseImageBaseChangeMap_paste_vert_app (sqT : IsPullback k f' f l)
    (sqB : IsPullback l g' g m) (hT : TorIndependent f l) (hB : TorIndependent g m)
    (K : quasiCoherentDerivedCategory Z) :
    haveI := isIso_twistedInverseImagePushforwardBaseChange_of_paste_vert sqT sqB hT hB
    (twistedInverseImageBaseChangeMap k (f' ≫ g') (f ≫ g) m
        (isQuasicoherent_homology_derivedPushforward_of_qcqs k)
        (isQuasicoherent_homology_derivedPushforward_of_qcqs (f ≫ g))
        (isQuasicoherent_homology_derivedPushforward_of_qcqs (f' ≫ g'))
        (isQuasicoherent_homology_derivedPushforward_of_qcqs m)
        (sqT.paste_vert sqB)).app K =
      (quasiCoherentDerivedPullback' k).map
          ((twistedInverseImageCompIso f g (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
            (isQuasicoherent_homology_derivedPushforward_of_qcqs g)
            (isQuasicoherent_homology_derivedPushforward_of_qcqs (f ≫ g))).hom.app K) ≫
        (torIndependentTwistedInverseImageBaseChange sqT hT).app
          ((twistedInverseImage g (isQuasicoherent_homology_derivedPushforward_of_qcqs g)).obj K) ≫
        (twistedInverseImage f' (isQuasicoherent_homology_derivedPushforward_of_qcqs f')).map
          ((torIndependentTwistedInverseImageBaseChange sqB hB).app K) ≫
        (twistedInverseImageCompIso f' g'
            (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
            (isQuasicoherent_homology_derivedPushforward_of_qcqs g')
            (isQuasicoherent_homology_derivedPushforward_of_qcqs (f' ≫ g'))).inv.app
          ((quasiCoherentDerivedPullback' m).obj K)
```

## Tag 0ATR, a lemma

[Tag 0ATR](https://stacks.math.columbia.edu/tag/0ATR) in the Stacks Project.

**`Stacks.Duality.twistedInverseImageBaseChangeMap_hcomp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BaseChangeHorizontal.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BaseChangeHorizontal.lean#L401). The attribute's comment: “for the base change map of Stacks 0AA6 attached to the twisted inverse image f^x of Stacks 0A9E -- the right adjoint of Rf_* on D_QCoh: the map of the outer rectangle of a row of two cartesian squares is the vertical composite of the maps of the two squares, read through the composition formula for derived pullback along the two composite horizontal morphisms. The source's quasi-compactness and quasi-separatedness enter as the preservation of quasi-coherent cohomology by derived direct and inverse image along the morphisms of the diagram and as the existence of the three right adjoints, which is what Stacks 08D5 part (1) and Stacks 0A9E produce for a quasi-compact quasi-separated morphism. Invertibility of the transformation xi of Stacks 0A9K for each of the two squares is an instance argument, exactly as in Stacks.Duality.twistedInverseImageBaseChangeMap where the base change map is defined, and it is Stacks 0A9K that produces it for a Tor-independent square; the rectangle's needs no third input, by Stacks.Duality.isIso_twistedInverseImagePushforwardBaseChange_hcomp”.

> **[Stacks, Tag 0ATR] (Lemma 48.5.2): the base change maps of a row of two cartesian squares
> compose to the base change map of the outer rectangle.** For
>
> ```
> X'' --k'--> X' --k--> X
> |f''        |f'       |f
> Y'' --l'--> Y' --l--> Y
> ```
>
> with both squares cartesian, the base change map `Stacks.Duality.twistedInverseImageBaseChangeMap`
> of [Stacks, Tag 0AA6] for the rectangle — the square with horizontal edges `k' ≫ k` and `l' ≫ l` —
> is the vertical paste of the base change maps of the right and of the left square, the derived
> pullbacks along the two composite horizontals being read through the composition formula
> `Stacks.Duality.quasiCoherentDerivedPullbackCompIsoConj`.
>
> Each base change map is the mate of the inverse of the corresponding `ξ`
> (`Stacks.Duality.twistedInverseImageBaseChangeMap_eq_mateEquiv_symm`), the rectangle's `ξ` is
> the vertical paste of the two (`Stacks.Duality.twistedInverseImagePushforwardBaseChange_hcomp`),
> and the inverse of a vertical paste is the horizontal paste of the inverses; the passage between
> the two pastes is `Stacks.Cohomology.DerivedBaseChangePasting.mate_twoSquare_paste`, with the
> composite adjunctions traded through the composition formulas, which are conjugate by
> construction.

```lean
theorem twistedInverseImageBaseChangeMap_hcomp (sq₁ : IsPullback k' f'' f' l')
    (sq₂ : IsPullback k f' f l)
    [IsIso (twistedInverseImagePushforwardBaseChange k' f'' f' l' hpushk' hpushf' hpushf''
      hpushl' sq₁)]
    [IsIso (twistedInverseImagePushforwardBaseChange k f' f l hpushk hpushf hpushf' hpushl sq₂)] :
    letI := isIso_twistedInverseImagePushforwardBaseChange_hcomp k' k f'' f' f l' l hpushk'
      hpushk hpushkk hpushf'' hpushf' hpushf hpushl' hpushl hpushll sq₁ sq₂
    twistedInverseImageBaseChangeMap (k' ≫ k) f'' f (l' ≫ l) hpushkk hpushf hpushf'' hpushll
        (sq₁.paste_horiz sq₂) =
      (((TwoSquare.mk _ _ _ _ (twistedInverseImageBaseChangeMap k f' f l hpushk hpushf hpushf'
              hpushl sq₂) ≫ᵥ
          TwoSquare.mk _ _ _ _ (twistedInverseImageBaseChangeMap k' f'' f' l' hpushk' hpushf'
            hpushf'' hpushl' sq₁)).whiskerLeft
        (quasiCoherentDerivedPullbackCompIsoConj l' l hpushl' hpushl hpushll
          (isQuasicoherent_homology_derivedPullback' l')
          (isQuasicoherent_homology_derivedPullback' l)
          (isQuasicoherent_homology_derivedPullback' (l' ≫ l))).hom).whiskerRight
        (quasiCoherentDerivedPullbackCompIsoConj k' k hpushk' hpushk hpushkk
          (isQuasicoherent_homology_derivedPullback' k')
          (isQuasicoherent_homology_derivedPullback' k)
          (isQuasicoherent_homology_derivedPullback' (k' ≫ k))).inv).natTrans
```

**`Stacks.Duality.twistedInverseImageBaseChangeMap_paste_horiz_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/TorIndependentBaseChangePasteHoriz.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/TorIndependentBaseChangePasteHoriz.lean#L191).

> **[Stacks, Tag 0ATR].** Consider a commutative diagram
> ```
> X'' --g'--> X' --g--> X
>  |          |         |
> f''         f'        f
>  v          v         v
> Y'' --h'--> Y' --h--> Y
> ```
> of quasi-compact and quasi-separated schemes in which both squares are cartesian, `f` and `h`
> are Tor independent and `f'` and `h'` are Tor independent. Then the base change maps
> (Equation 48.5.0.1 of [Stacks, Tag 0AA6]) of the two squares compose to the base change map of
> the outer rectangle: with `k = g' ≫ g`, `m = h' ≫ h` and `a`, `a'`, `a''` the right adjoints of
> `Rf_*`, `Rf'_*`, `Rf''_*`, for every `K ∈ D_QCoh(𝒪_Y)` the map `Lk^* a(K) ⟶ a''(Lm^* K)` of the
> rectangle is
>
> ```
> Lk^* a(K) = L(g')^* Lg^* a(K) ⟶ L(g')^* a'(Lh^* K) ⟶ a''(L(h')^* Lh^* K) = a''(Lm^* K),
> ```
>
> the identifications being the composition isomorphisms of derived pullback. The base change map
> of the rectangle is defined because its `ξ` is invertible,
> `Stacks.Duality.isIso_twistedInverseImagePushforwardBaseChange_of_paste_horiz`.

```lean
theorem twistedInverseImageBaseChangeMap_paste_horiz_app (sqR : IsPullback g f' f h)
    (sqL : IsPullback g' f'' f' h') (hR : TorIndependent f h) (hL : TorIndependent f' h')
    (K : quasiCoherentDerivedCategory Y) :
    haveI := isIso_twistedInverseImagePushforwardBaseChange_of_paste_horiz sqR sqL hR hL
    (twistedInverseImageBaseChangeMap (g' ≫ g) f'' f (h' ≫ h)
        (isQuasicoherent_homology_derivedPushforward_of_qcqs (g' ≫ g))
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f'')
        (isQuasicoherent_homology_derivedPushforward_of_qcqs (h' ≫ h))
        (sqL.paste_horiz sqR)).app K =
      (quasiCoherentDerivedPullbackCompIso g' g).inv.app
          ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj K) ≫
        (quasiCoherentDerivedPullback' g').map
          ((torIndependentTwistedInverseImageBaseChange sqR hR).app K) ≫
        (torIndependentTwistedInverseImageBaseChange sqL hL).app
          ((quasiCoherentDerivedPullback' h).obj K) ≫
        (twistedInverseImage f'' (isQuasicoherent_homology_derivedPushforward_of_qcqs f'')).map
          ((quasiCoherentDerivedPullbackCompIso h' h).hom.app K)
```

## Tag 0ATS, a remark

[Tag 0ATS](https://stacks.math.columbia.edu/tag/0ATS) in the Stacks Project.

**`Stacks.Duality.twistedInverseImageBaseChangeMap_grid_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/TorIndependentBaseChangeGrid.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/TorIndependentBaseChangeGrid.lean#L169).

> **[Stacks, Tag 0ATS].** Consider a commutative diagram
> ```
> X'' --k'--> X' --k--> X
>  |          |         |
> f''         f'        f
>  v          v         v
> Y'' --l'--> Y' --l--> Y
>  |          |         |
> g''         g'        g
>  v          v         v
> Z'' --m'--> Z' --m--> Z
> ```
> of quasi-compact and quasi-separated schemes in which all squares are cartesian and
> `(f, l)`, `(g, m)`, `(f', l')`, `(g', m')` are Tor independent pairs. Let `a, a', a''`,
> `b, b', b''` be the right adjoints of `Rf_*, Rf'_*, Rf''_*`, `Rg_*, Rg'_*, Rg''_*`
> ([Stacks, Tag 0A9E]); label the squares `A` (top left), `B` (top right), `C` (bottom left) and
> `D` (bottom right). The base change maps (Equation 48.5.0.1 of [Stacks, Tag 0AA6]) of the four
> rectangles made of two squares give two transformations
> `L(k')^* Lk^* a b ⟶ a'' b'' L(m')^* Lm^*`, namely `γ_{A+C} ∘ γ_{B+D}` and `γ_{C+D} ∘ γ_{A+B}`, and
> these are equal: for every `K ∈ D_QCoh(𝒪_Z)`,
>
> * `γ_{A+C} ∘ γ_{B+D}` is `L(k')^* Lk^* a(b(K)) ≅ L(k')^* Lk^* c(K) ⟶ L(k')^* c'(Lm^* K) ⟶
>   c''(L(m')^* Lm^* K) ≅ a''(b''(L(m')^* Lm^* K))`, with `c, c', c''` the right adjoints of
>   `R(f ≫ g)_*, R(f' ≫ g')_*, R(f'' ≫ g'')_*` identified with `b ⋙ a`, … by
>   [Stacks, Tag 0ATX];
> * `γ_{C+D} ∘ γ_{A+B}` is `L(k')^* Lk^* a(b(K)) ≅ L(k' ≫ k)^* a(b(K)) ⟶ a''(L(l' ≫ l)^* b(K)) ⟶
>   a''(b''(L(m' ≫ m)^* K)) ≅ a''(b''(L(m')^* Lm^* K))`, through the composition isomorphisms
>   of derived pullback.
>
> The base change maps of the rectangles are defined because their `ξ` are invertible
> ([Stacks, Tag 0ATR], [Stacks, Tag 0ATQ]).

```lean
theorem twistedInverseImageBaseChangeMap_grid_app
    (sqA : IsPullback k' f'' f' l') (sqB : IsPullback k f' f l)
    (sqC : IsPullback l' g'' g' m') (sqD : IsPullback l g' g m)
    (hB : TorIndependent f l) (hD : TorIndependent g m) (hA : TorIndependent f' l')
    (hC : TorIndependent g' m') (K : quasiCoherentDerivedCategory Z) :
    haveI := isIso_twistedInverseImagePushforwardBaseChange_of_paste_vert sqB sqD hB hD
    haveI := isIso_twistedInverseImagePushforwardBaseChange_of_paste_vert sqA sqC hA hC
    haveI := isIso_twistedInverseImagePushforwardBaseChange_of_paste_horiz sqB sqA hB hA
    haveI := isIso_twistedInverseImagePushforwardBaseChange_of_paste_horiz sqD sqC hD hC
    (quasiCoherentDerivedPullback' k').map ((quasiCoherentDerivedPullback' k).map
        ((twistedInverseImageCompIso f g (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g)
          (isQuasicoherent_homology_derivedPushforward_of_qcqs (f ≫ g))).inv.app K)) ≫
      (quasiCoherentDerivedPullback' k').map
        ((twistedInverseImageBaseChangeMap k (f' ≫ g') (f ≫ g) m
          (isQuasicoherent_homology_derivedPushforward_of_qcqs k)
          (isQuasicoherent_homology_derivedPushforward_of_qcqs (f ≫ g))
          (isQuasicoherent_homology_derivedPushforward_of_qcqs (f' ≫ g'))
          (isQuasicoherent_homology_derivedPushforward_of_qcqs m)
          (sqB.paste_vert sqD)).app K) ≫
      (twistedInverseImageBaseChangeMap k' (f'' ≫ g'') (f' ≫ g') m'
          (isQuasicoherent_homology_derivedPushforward_of_qcqs k')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs (f' ≫ g'))
          (isQuasicoherent_homology_derivedPushforward_of_qcqs (f'' ≫ g''))
          (isQuasicoherent_homology_derivedPushforward_of_qcqs m')
          (sqA.paste_vert sqC)).app ((quasiCoherentDerivedPullback' m).obj K) ≫
      (twistedInverseImageCompIso f'' g''
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f'')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g'')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs (f'' ≫ g''))).hom.app
        ((quasiCoherentDerivedPullback' m').obj ((quasiCoherentDerivedPullback' m).obj K)) =
    (quasiCoherentDerivedPullbackCompIso k' k).hom.app
        ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
          ((twistedInverseImage g (isQuasicoherent_homology_derivedPushforward_of_qcqs g)).obj
            K)) ≫
      (twistedInverseImageBaseChangeMap (k' ≫ k) f'' f (l' ≫ l)
          (isQuasicoherent_homology_derivedPushforward_of_qcqs (k' ≫ k))
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f'')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs (l' ≫ l))
          (sqA.paste_horiz sqB)).app
        ((twistedInverseImage g (isQuasicoherent_homology_derivedPushforward_of_qcqs g)).obj K) ≫
      (twistedInverseImage f'' (isQuasicoherent_homology_derivedPushforward_of_qcqs f'')).map
        ((twistedInverseImageBaseChangeMap (l' ≫ l) g'' g (m' ≫ m)
          (isQuasicoherent_homology_derivedPushforward_of_qcqs (l' ≫ l))
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g)
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g'')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs (m' ≫ m))
          (sqC.paste_horiz sqD)).app K) ≫
      (twistedInverseImage f'' (isQuasicoherent_homology_derivedPushforward_of_qcqs f'')).map
        ((twistedInverseImage g'' (isQuasicoherent_homology_derivedPushforward_of_qcqs g'')).map
          ((quasiCoherentDerivedPullbackCompIso m' m).inv.app K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.5, Tag 0AA5](https://stacks.math.columbia.edu/tag/0AA5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
