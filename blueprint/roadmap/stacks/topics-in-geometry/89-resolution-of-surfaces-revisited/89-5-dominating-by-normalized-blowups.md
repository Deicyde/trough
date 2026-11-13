---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsNormalizedBlowupAtClosedPoint, AlgebraicGeometry.Space.NormalizedBlowupAtClosedPoint.isNormal_and_isNagata_and_isProper_of_isNagata, AlgebraicGeometry.Space.NormalizedBlowupFactorization, AlgebraicGeometry.Space.ClosedPointNeighborhoods.GlobalNormalizedBlowupFactorization, AlgebraicGeometry.Space.ClosedPointNeighborhoods.LocalNormalizedBlowupFactorization, AlgebraicGeometry.Space.ClosedPointNeighborhoods.nonempty_globalNormalizedBlowupFactorization_iff, Stacks.Examples.NormalizedBlowupsNotEtaleLocal.not_stacks0BHL, AlgebraicGeometry.Space.exists_normalizedBlowUpChain_dominating
statement: formalized
proof: formalized
---

# 89.5 Dominating by normalized blowups

Section 89.5 of the Stacks Project, [Tag 0BHI](https://stacks.math.columbia.edu/tag/0BHI). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BHJ, a definition

[Tag 0BHJ](https://stacks.math.columbia.edu/tag/0BHJ) in the Stacks Project.

**`AlgebraicGeometry.Space.IsNormalizedBlowupAtClosedPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizedBlowupsAtClosedPoints.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NormalizedBlowupsAtClosedPoints.lean#L185).

> **Stacks 0BHJ.** A morphism `f : X'' ⟶ X` of algebraic spaces **is the normalized blowing up
> of `X` at the closed point `z`** when it is the composition of the normalization of a blowing up
> of `X` at `z` with that blowing up: there are an algebraic space `X'`, a blowing up `b : X' ⟶ X`
> of `X` at `z`, normalization data on `X'`, and an identification of `X''` with the normalization
> carrying `f` to the normalization morphism followed by `b`.
>
> The blowing up at `z` is `AlgebraicGeometry.Space.IsBlowupAtClosedPoint`, and the normalization
> is the datum `AlgebraicGeometry.Space.NormalizationData`.  The decency hypothesis and the
> finiteness condition of Stacks 0BB1 are those of the source.

```lean
def IsNormalizedBlowupAtClosedPoint {X Y : AlgebraicSpaces B S hS}
    (_hX : IsDecentSpace B S hS X.obj)
    (_hXfin : HasLocallyFiniteIrreducibleComponents B S hS X.obj)
    (z : points B S hS X.obj) (hz : IsClosed ({z} : Set (points B S hS X.obj)))
    (f : Y ⟶ X) : Prop
```

## Tag 0BHK, a lemma

[Tag 0BHK](https://stacks.math.columbia.edu/tag/0BHK) in the Stacks Project.

**`AlgebraicGeometry.Space.NormalizedBlowupAtClosedPoint.isNormal_and_isNagata_and_isProper_of_isNagata`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizedBlowupAtClosedPointProper.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NormalizedBlowupAtClosedPointProper.lean#L134). The attribute's comment: “the lemma in full, with NOTHING carried: for a Nagata X, every normalized blowing up of X at a closed point is an algebraic space, normal, Nagata, and proper over X”.

> **Stacks 0BHK.**  If `X` is Nagata, then the normalized blowing up of `X` at a closed point
> `z` is a normal Nagata algebraic space proper over `X`.
>
> Spelled out: for every normalized blowing up `X'' ⟶ X' ⟶ X` of `X` at `z` (Stacks 0BHJ), `X''`
> is an algebraic space over `S`, it is normal, it is Nagata, and the composite `X'' ⟶ X` is
> proper.  The only hypothesis is that `X` is Nagata.
>
> The proof is the source's.  The blowing up `X' ⟶ X` is proper,
> `AlgebraicGeometry.Space.NormalizedBlowupAtClosedPoint.isProper_proj` (Stacks 085Z, `X` being
> locally Noetherian); hence `X'` is Nagata (Stacks 0BAU), the normalization `X'' ⟶ X'` is finite
> (Stacks 0BB5), hence proper (Stacks 04NZ), and the composite is proper (Stacks 04XY); `X''` is
> normal by Stacks 0BB4 and Nagata by Stacks 0BAU again.

```lean
theorem isNormal_and_isNagata_and_isProper_of_isNagata
    (hNagata : HasEtaleLocalProperty B S hS X.obj (fun T : Scheme.{u} => IsNagataScheme T)) :
    IsAlgebraicSpace B S hS N.space.obj ∧
      HasEtaleLocalProperty B S hS N.space.obj
        (fun T : Scheme.{u} => _root_.AlgebraicGeometry.IsNormal T) ∧
      HasEtaleLocalProperty B S hS N.space.obj (fun T : Scheme.{u} => IsNagataScheme T) ∧
      IsProper B S hS N.hom.hom
```

## Tag 0BHL, a lemma

[Tag 0BHL](https://stacks.math.columbia.edu/tag/0BHL) in the Stacks Project.

**`AlgebraicGeometry.Space.NormalizedBlowupFactorization`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizedBlowupsAtClosedPoints.lean, line 427](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NormalizedBlowupsAtClosedPoints.lean#L427). The attribute's comment: “the condition asserted on both sides of the equivalence: a factorization of the given morphism as a finite sequence of normalized blowings up at closed points lying over the given set of points. The equivalence itself is not proved: its proof is the argument of Tag 0BHF, which this library does carry, together with a comparison of a normalization with an étale base change of it, which it does not.”.

> **A factorization of `f : Y ⟶ X` as a sequence of normalized blowings up at closed points
> lying over the set of points `T ⊆ |X|`**: a tower
>
> `Zₘ ⟶ Zₘ₋₁ ⟶ … ⟶ Z₁ ⟶ Z₀ = X`
>
> of normalized blowings up at closed points, all of whose centres lie over `T`, together with an
> identification of `Y` with its top `Zₘ` under which `f` is the composite `Zₘ ⟶ X`.
>
> This is the condition on both sides of Stacks 0BHL, taken there with `T = {x₁, …, xₙ}` for the
> morphism to `X` and with `T = {uᵢ}` for the morphism to the `i`th étale neighborhood.

```lean
structure NormalizedBlowupFactorization (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X Y : AlgebraicSpaces B S hS} (T : Set (points B S hS X.obj))
    (f : Y ⟶ X)
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.GlobalNormalizedBlowupFactorization`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizedBlowupsAtClosedPoints.lean, line 526](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NormalizedBlowupsAtClosedPoints.lean#L526). The attribute's comment: “the left-hand side of the equivalence: the factorization of the morphism to X by normalized blowings up at closed points lying over \{x₁, …, xₙ}”.

> **Stacks 0BHL**, the condition on the morphism to `X`: `f : Y ⟶ X` factors as
>
> `Y = Zₘ ⟶ Zₘ₋₁ ⟶ … ⟶ Z₁ ⟶ Z₀ = X`
>
> where each `Z_{j+1} ⟶ Z_j` is the normalized blowing up of `Z_j` at a closed point `z_j` lying
> over `{x₁, …, xₙ}`.

```lean
abbrev GlobalNormalizedBlowupFactorization {Y : AlgebraicSpaces B S hS} (f : Y ⟶ D.space)
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.LocalNormalizedBlowupFactorization`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizedBlowupsAtClosedPoints.lean, line 538](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NormalizedBlowupsAtClosedPoints.lean#L538). The attribute's comment: “the right-hand side of the equivalence: the factorization of the morphism to the i-th elementary étale neighborhood by normalized blowings up at closed points lying over uᵢ”.

> **Stacks 0BHL**, the condition on the morphism to the `i`th étale neighborhood:
> `gᵢ : Yᵢ ⟶ Uᵢ` factors as
>
> `Yᵢ = Z_{i, mᵢ} ⟶ … ⟶ Z_{i, 1} ⟶ Z_{i, 0} = Uᵢ`
>
> where each `Z_{i, j+1} ⟶ Z_{i, j}` is the normalized blowing up of `Z_{i, j}` at a closed point
> lying over `uᵢ`.

```lean
abbrev LocalNormalizedBlowupFactorization (i : Fin n) {Y : AlgebraicSpaces B S hS}
    (g : Y ⟶ D.neighborhoodSpace i)
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.nonempty_globalNormalizedBlowupFactorization_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizedBlowupsAtClosedPointsEquivalence.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NormalizedBlowupsAtClosedPointsEquivalence.lean#L249). The attribute's comment: “corrected (erratum): with X normal; false as written without it, the normalized blowup normalizes the whole space (counterexamples to both directions in the module documentation); otherwise the full statement, under the source's hypotheses”.

> **Stacks 0BHL, for normal `X`.** Let `X, xᵢ, Uᵢ ⟶ X, uᵢ` be as in Stacks 0BHA and let
> `f : Y ⟶ X` correspond to `gᵢ : Yᵢ ⟶ Uᵢ` under the functor `F` of Stacks 0BHA. Assume that `X`
> satisfies the equivalent conditions of Stacks 0BB1 and that `X` is normal. Then `f` factors as
> `Y = Zₘ ⟶ … ⟶ Z₁ ⟶ Z₀ = X` with each `Z_{j+1} ⟶ Z_j` the normalized blowing up of `Z_j` at a
> closed point over `{x₁, …, xₙ}` if and only if each `gᵢ` factors as
> `Yᵢ = Z_{i, mᵢ} ⟶ … ⟶ Z_{i, 0} = Uᵢ` with each step the normalized blowing up at a closed point
> over `uᵢ`.
>
> The normality of `X` is not in the source, but the statement is false without it; see the module
> documentation for a counterexample to each direction.

```lean
theorem nonempty_globalNormalizedBlowupFactorization_iff
    (hXfin : HasLocallyFiniteIrreducibleComponents B S hS D.space.obj)
    (hXn : Space.IsNormal B S hS D.space.obj) (M : D.modificationsAwayFromPoints)
    (N : ∀ i, D.modificationsAt i) (e : D.restrictionFunctor.obj M ≅ N) :
    Nonempty (D.GlobalNormalizedBlowupFactorization (ObjectProperty.homMk M.obj.hom :
        (⟨M.obj.left, M.property.1⟩ : AlgebraicSpaces B S hS) ⟶ D.space)) ↔
      ∀ i, Nonempty (D.LocalNormalizedBlowupFactorization i (ObjectProperty.homMk (N i).obj.hom :
        (⟨(N i).obj.left, (N i).property.1⟩ : AlgebraicSpaces B S hS) ⟶
          D.neighborhoodSpace i))
```

**`Stacks.Examples.NormalizedBlowupsNotEtaleLocal.not_stacks0BHL`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/NormalizedBlowupsNotEtaleLocal.lean, line 555](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/NormalizedBlowupsNotEtaleLocal.lean#L555). The attribute's comment: “refutation of the published statement: false without X normal; at X = Spec(Z/36Z), two closed points with non-reduced local rings, g₁ the normalized blowing up of U₁ at u₁ and g₂ = id are sequences of normalized blowings up, but the f corresponding to them is not, a nonempty sequence having a normal source and the empty one being an isomorphism”.

> **Stacks 0BHL is false as published.** The source asserts, for every scheme `S`, every
> decent algebraic space `X` over `S` satisfying the equivalent conditions of Stacks 0BB1, every
> choice of pairwise distinct closed points `x₁, …, xₙ` and elementary étale neighbourhoods
> `(Uᵢ, uᵢ) ⟶ (X, xᵢ)` as in Stacks 0BHA, and every `f : Y ⟶ X` corresponding to `gᵢ : Yᵢ ⟶ Uᵢ`
> under the functor `F` of Stacks 0BHA, that `f` is a sequence of normalized blowings up at closed
> points over `{x₁, …, xₙ}` if and only if each `gᵢ` is one at closed points over `uᵢ`. This is
> the negation of that assertion, with exactly its hypotheses; `exists_counterexample` is a
> counterexample to the "if" direction.
>
> The statement holds once `X` is normal: this is `nonempty_globalNormalizedBlowupFactorization_iff`
> in the namespace `AlgebraicGeometry.Space.ClosedPointNeighborhoods`.

```lean
theorem not_stacks0BHL :
    ¬ ∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) (n : ℕ)
      (D : ClosedPointNeighborhoods B S hS n)
      (_ : HasLocallyFiniteIrreducibleComponents B S hS D.space.obj)
      (M : D.modificationsAwayFromPoints) (N : ∀ i, D.modificationsAt i)
      (_ : D.restrictionFunctor.obj M ≅ N),
      Nonempty (D.GlobalNormalizedBlowupFactorization (ObjectProperty.homMk M.obj.hom :
          (⟨M.obj.left, M.property.1⟩ : AlgebraicSpaces B S hS) ⟶ D.space)) ↔
        ∀ i, Nonempty (D.LocalNormalizedBlowupFactorization i
          (ObjectProperty.homMk (N i).obj.hom :
            (⟨(N i).obj.left, (N i).property.1⟩ : AlgebraicSpaces B S hS) ⟶
              D.neighborhoodSpace i))
```

## Tag 0BHM, a lemma

[Tag 0BHM](https://stacks.math.columbia.edu/tag/0BHM) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_normalizedBlowUpChain_dominating`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SurfaceTransfer/DominatingNormalizedBlowups.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SurfaceTransfer/DominatingNormalizedBlowups.lean#L167).

> **Stacks 0BHM.** Let `S` be a scheme, let `X` be a Noetherian Nagata algebraic space over
> `S` with `dim(X) = 2`, and let `f : Y ⟶ X` be a proper birational morphism. Then there is a
> commutative diagram
>
> ```
> X_n ⟶ X_{n-1} ⟶ … ⟶ X_1 ⟶ X_0
>  |                            |
>  v                            v
>  Y  ------------------------> X
> ```
>
> where `X_0 ⟶ X` is the normalization and `X_{i+1} ⟶ X_i` is the normalized blowing up of `X_i`
> at a closed point: a sequence `NormalizedBlowUpChain B S hS X A g` with top `A = X_n` and
> composite `g : X_n ⟶ X`, and `h : X_n ⟶ Y` with `h ≫ f = g`.
>
> Being Noetherian is Stacks 03EA (quasi-compact, quasi-separated, locally Noetherian), Nagata is
> the étale-local property of Stacks 03E6, `dim(X)` is Stacks 04N6, properness is Stacks 04XU, and
> birationality is Stacks 0ACV, which is defined for decent spaces with finitely many irreducible
> components; those witnesses are carried existentially, being consequences of the Noetherian
> hypothesis and of properness rather than extra assumptions.

```lean
theorem exists_normalizedBlowUpChain_dominating {X Y : AlgebraicSpaces B S hS}
    (hXN : IsNoetherian B S hS B.contains_terminal X.obj)
    (hXnag : HasEtaleLocalProperty B S hS X.obj (fun T : Scheme.{u} => IsNagataScheme T))
    (hXdim : dimension B S hS X.obj X.property = 2) (f : Y ⟶ X)
    (hf : IsProper B S hS f.hom)
    (hbir : ∃ (hDY : IsDecentSpace B S hS Y.obj) (hDX : IsDecentSpace B S hS X.obj)
      (hCY : (irreducibleComponents (points B S hS Y.obj)).Finite)
      (hCX : (irreducibleComponents (points B S hS X.obj)).Finite),
      IsBirational B S hS Y.property X.property hDY hDX hCY hCX f.hom) :
    ∃ (A : AlgebraicSpaces B S hS) (g : A ⟶ X) (h : A ⟶ Y),
      NormalizedBlowUpChain B S hS X A g ∧ h ≫ f = g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 89.5, Tag 0BHI](https://stacks.math.columbia.edu/tag/0BHI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
