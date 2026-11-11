---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.PrimeDivisor.genericResidueFieldEquivFunctionField, AlgebraicGeometry.Space.PrimeDivisor.henselianResidueFieldEquivFunctionField, AlgebraicGeometry.Space.PrimeDivisor.genericRestriction, AlgebraicGeometry.Space.firstChernCapCycleMap_divisorCycleAt_eq_componentDivisorSum, AlgebraicGeometry.Space.firstChernCapCycleMap_divisorCycleAt_eq_componentDivisorSum_of_isInvertible, AlgebraicGeometry.Space.canonicalFirstChernCap_divisor_comm, AlgebraicGeometry.Space.canonicalFirstChernCap_canonicalDivisorCycleAt, AlgebraicGeometry.Space.locallyFinite_primeDivisor_not_sectionGenerates
statement: formalized
proof: formalized
---

# 82.20 The key formula

Section 82.20 of the Stacks Project, [Tag 0EQU](https://stacks.math.columbia.edu/tag/0EQU). 2 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EQU, the section

[Tag 0EQU](https://stacks.math.columbia.edu/tag/0EQU) in the Stacks Project.

**`AlgebraicGeometry.Space.PrimeDivisor.genericResidueFieldEquivFunctionField`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormula/GenericResidueField.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormula/GenericResidueField.lean#L188). The attribute's comment: “the identification κ(ξ) = R(Z) of the residue field at the generic point of a prime divisor with its function field, at the residue field of the chosen chart”.

> **The canonical isomorphism `θ_Z : κ(u) ≃+* R(Z)`** of Section 0EQU between the residue
> field of the local ring of the chart at the generic point of a prime divisor and the function
> field of the prime divisor.  Its inverse is evaluation at `ρ_Z`.

```lean
def PrimeDivisor.genericResidueFieldEquivFunctionField :
    Z.genericResidueField B S hS hX hdec ≃+* rationalFunctions B S hS Z.closed.1
```

**`AlgebraicGeometry.Space.PrimeDivisor.henselianResidueFieldEquivFunctionField`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormula/GenericResidueField.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormula/GenericResidueField.lean#L306). The attribute's comment: “the residue field of the henselian local ring at the generic point of a prime divisor is its function field”.

> **The composite `κ(𝒪^h_{X, ξ}) ≃+* R(Z)`**: the residue field of the henselian local ring at
> the generic point of a prime divisor is the function field of the prime divisor, through the
> residue field `κ(u)` of the chosen chart.  A unit `v` of `𝒪^h_{X, ξ}` thus has a residue
> `θ(v̄) ∈ R(Z)`, which is how the key formula of Section 0EQU reads a change of generator on
> `Z`.

```lean
def PrimeDivisor.henselianResidueFieldEquivFunctionField :
    letI := henselianLocalRing_isLocalRing B S hS X hX (Z.genericPoint B S hS X) hdec
    IsLocalRing.ResidueField ↥(Z.genericHenselianLocalRing B S hS hX hdec) ≃+*
      rationalFunctions B S hS Z.closed.1
```

**`AlgebraicGeometry.Space.PrimeDivisor.genericRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormula/GenericRestriction.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormula/GenericRestriction.lean#L268). The attribute's comment: “the image s\_ξ|\_Z of a generator s\_ξ of ℒ\_ξ in the fibre at the generic point, as a meromorphic section of ℒ|\_Z”.

> **`σ_Z = s_ξ|_Z`, the restriction to a prime divisor of the generator at its generic point**:
> the unique meromorphic section of `ℒ|_Z` whose pullback along `ρ_Z : Spec κ(u) → Z` is the image
> of the generator `s_ξ` of `ℒ` at the generic point.

```lean
def PrimeDivisor.genericRestriction :
    MeromorphicSection.{u, u} B S hS Z.subspace.toFunctor Z.closed.1
      (Z.restrictModule B S hS hX L)
```

**`AlgebraicGeometry.Space.firstChernCapCycleMap_divisorCycleAt_eq_componentDivisorSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormulaComponentDivisor.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormulaComponentDivisor.lean#L420). The attribute's comment: “either cycle identity of the section, c\_1(N) ∩ div\_L(s) = ∑ ord\_\{B\_i}(f\_i) (Z\_i → X)\_* div\_\{N|Z\_i}(t\_i|Z\_i) in Z\_\{n-2}(X), with the component cycle no longer a parameter: it is the Weil divisor div\_\{N|W}(t\_W) of Stacks 0EQE part (1) on W, for the restriction N|W of Stacks 03LU. N is arbitrary here, and what is then carried on W is what Stacks 0EQE carries on X: the meromorphic section t W, the Stacks 0EPR ratio family, the Stacks 0EPS local finiteness and the Stacks 0EDN dimension function. For N invertible, which is the section's own hypothesis, t W and the dimension function are produced and not carried, see firstChernCapCycleMap\_divisorCycleAt\_eq\_componentDivisorSum\_of\_isInvertible. hdim is Stacks 0EPZ. The key formula 0EQV IS proved, unconditionally and axiom-clean, as keyFormula\_of\_ne\_zero of StacksFrontier.AlgebraicGeometry.Spaces.Chow.KeyFormulaProof.Headline, and 0EQX follows there as canonicalFirstChernCap\_divisor\_comm; what is still open is only the quantified predicate KeyFormula of KeyFormulaCycleIdentities, which ranges over the component rules of 0EQJ and the tame-symbol divisors”.

> **Stacks 0EQU: either cycle identity of the section preceding the key formula, with the
> component cycle `div_{𝒩|Z_i}(t_i|Z_i)` constructed and not assumed.**  In Situation 0EDT let
> `X/B` be good and integral with `dim_δ(X) = n`, let `ℒ` and `𝒩` be `𝒪_X`-modules, let `s` be a
> nonzero meromorphic section of `ℒ`, and let `{Z_i}`, `i ∈ I`, be an injective locally finite
> family of prime divisors of `X` containing every prime divisor along which `s` has nonzero order
> of vanishing.  Then
>
> `c₁(𝒩) ∩ div_ℒ(s) = ∑_i ord_{Z_i,ℒ}(s) · (Z_i → X)_* div_{𝒩|Z_i}(t_i|Z_i)`
>
> in `Z_{n-2}(X)`, the component cycle `c₁(𝒩|_{Z_i}) ∩ [Z_i]` being the Weil divisor
> `div_{𝒩|Z_i}(t_i|Z_i)` of Stacks 0EQE part (1) on `Z_i`, that is
> `AlgebraicGeometry.Space.componentDivisorCycleRule`.  The two identities displayed in Section
> 0EQU before the key formula are the two instances of this statement, exchanging `(ℒ, s)` with
> `(𝒩, t)` and `𝒩` with `ℒ`.
>
> The orders `ord_{Z_i,ℒ}(s)` are those of Stacks 0EPR, which the source identifies with its
> `ord_{B_i}(f_i)`; the δ-dimension hypothesis `hdim` is Stacks 0EPZ, proved as
> `AlgebraicGeometry.Space.deltaDimension_toIntegralClosedSubspace`.
>
> This statement takes, as inputs on each `W`, exactly what Stacks 0EQE takes on `X`: the
> meromorphic section `t W` of `𝒩|_W`, which at `W = Z_i` is the source's reduction `t_i|Z_i`
> (`AlgebraicGeometry.Space.PrimeDivisor.genericFibreReduction`, read through Stacks 0EN0); the
> ratio family `ratioN` of Stacks 0EPR; the local finiteness `hfinN` of Stacks 0EPS; and the
> dimension function `dimN` of Stacks 0EDN.  The same four, on `X`, are `ratio`, `hfin`, `d` and
> `hd` here.  Two of those four are no longer needed once `𝒩` is invertible, which is Section
> 0EQU's own hypothesis on `𝒩`:
> `firstChernCapCycleMap_divisorCycleAt_eq_componentDivisorSum_of_isInvertible`
> is this identity with `t` produced by Stacks 0EPQ on `W` and with `dimN` derived from `d`.  This
> version is kept because it needs no hypothesis on `𝒩` at all.
>
> The key formula itself, Stacks 0EQV, **is** proved, unconditionally and axiom-clean:
> `AlgebraicGeometry.Space.keyFormula_of_ne_zero` of
> `StacksFrontier.AlgebraicGeometry.Spaces.Chow.KeyFormulaProof.Headline`, at the canonical choices and
> for the constructed tame-symbol sum, from which Stacks 0EQX follows there as
> `AlgebraicGeometry.Space.canonicalFirstChernCap_divisor_comm`.  What is still open is only the
> *predicate* `AlgebraicGeometry.Space.KeyFormula` of
> `StacksFrontier.AlgebraicGeometry.Spaces.Chow.KeyFormulaCycleIdentities`, which quantifies the
> component rules of Stacks 0EQJ and the principal divisors of the tame symbols; at that generality
> it is not a theorem of this library.

```lean
theorem firstChernCapCycleMap_divisorCycleAt_eq_componentDivisorSum
    {k : ℤ} {I : Type v}
    (t : ∀ W : IntegralClosedSubspace D.site D.base D.base_mem X,
      MeromorphicSection.{u, u} D.site D.base D.base_mem W.subspace.toFunctor
        (setup.isSpace W) (integralClosedSubspaceRestrict D sX hX N W))
    (ratioN : ∀ W : IntegralClosedSubspace D.site D.base D.base_mem X,
      LocalRatioFamily.{u, u} D.site D.base D.base_mem (setup.isSpace W) (setup.isDecent W)
        (integralClosedSubspaceRestrict D sX hX N W))
    (dimN : ∀ W : IntegralClosedSubspace D.site D.base D.base_mem X,
      DimensionFunction (points D.site D.base D.base_mem W.subspace.toFunctor))
    (hdimN : ∀ (W : IntegralClosedSubspace D.site D.base D.base_mem X)
      (x : points D.site D.base D.base_mem W.subspace.toFunctor),
      dimN W x = D.deltaValue (W.subspace.ι ≫ sX) x)
    (hfinN : ∀ W : IntegralClosedSubspace D.site D.base D.base_mem X,
      LocallyFinite fun P : PrimeDivisor D.site D.base D.base_mem W.subspace.toFunctor =>
        if setup.sectionOrder W (integralClosedSubspaceRestrict D sX hX N W) (t W) (ratioN W) P = 0
          then ∅ else P.support D.site D.base D.base_mem W.subspace.toFunctor)
    (s : MeromorphicSection.{u, z} D.site D.base D.base_mem X hX.1 L)
    (ratio : LocalRatioFamily.{u, z} D.site D.base D.base_mem hX.1 hdec L)
    (hfin : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem X =>
      if divisorCoefficients.{u, z} D.site D.base D.base_mem hX.1 hdec L s ratio W = 0 then ∅
      else W.support D.site D.base D.base_mem X)
    (hint : IsIntegralSpace D.site D.base D.base_mem X)
    (d : DimensionFunction (points D.site D.base D.base_mem X))
    (hd : ∀ x, d x = D.deltaValue sX x) {n : ℤ}
    (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt))
    (hk : k + 1 = n - 1)
    (Z : I → PrimeDivisor D.site D.base D.base_mem X)
    (hZinj : Function.Injective Z)
    (hZfin : LocallyFinite fun i : I =>
      subspacePointSet D.site D.base D.base_mem X (Z i).subspace)
    (hdim : ∀ i, deltaDimension D sX
      ((Z i).toIntegralClosedSubspace D.site D.base D.base_mem) = k + 1)
    (hcover : ∀ W : PrimeDivisor D.site D.base D.base_mem X,
      divisorCoefficients.{u, z} D.site D.base D.base_mem hX.1 hdec L s ratio W ≠ 0 →
        ∃ i, Z i = W) :
    firstChernCapCycleMap D sX hX k
        (componentDivisorCycleRule sX hX setup N k t ratioN dimN hdimN hfinN)
        (divisorCycleAt.{u, z} D sX hX hdec L s ratio hfin hint d hd hn hk) =
      cycleFamilySum D sX hX
        (fun i => (Z i).toIntegralClosedSubspace D.site D.base D.base_mem) hZfin k
        (fun i => orderOfVanishingSection.{u, z} D.site D.base D.base_mem hX.1 hdec (Z i) L s
          (ratio (Z i)) •
            componentDivisorCycleRule sX hX setup N k t ratioN dimN hdimN hfinN
              ((Z i).toIntegralClosedSubspace D.site D.base D.base_mem) (hdim i))
```

**`AlgebraicGeometry.Space.firstChernCapCycleMap_divisorCycleAt_eq_componentDivisorSum_of_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormulaComponentDivisor.lean, line 597](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormulaComponentDivisor.lean#L597). The attribute's comment: “either cycle identity of the section for an invertible N, with the component cycle div\_\{N|W}(t\_W) of Stacks 0EQE part (1) on W and its meromorphic section t\_W no longer a parameter: t\_W is a regular meromorphic section of N|W produced by Stacks 0EPQ on W, and the Stacks 0EDN dimension function on W is the one on X pulled back along the closed embedding. What is carried on W is the Stacks 0EPR ratio family and the Stacks 0EPS local finiteness of the prime divisors of nonzero order, both blocked by LocalRatio being an unconstrained function type. hdim is Stacks 0EPZ. The key formula 0EQV IS proved, unconditionally and axiom-clean, as keyFormula\_of\_ne\_zero of StacksFrontier.AlgebraicGeometry.Spaces.Chow.KeyFormulaProof.Headline, and 0EQX follows there as canonicalFirstChernCap\_divisor\_comm; what is still open is only the quantified predicate KeyFormula of KeyFormulaCycleIdentities, which ranges over the component rules of 0EQJ and the tame-symbol divisors”.

> **Stacks 0EQU for an invertible `𝒩`, with the component cycle's meromorphic section and
> dimension function produced and not assumed.**  Section 0EQU's cycle identity
>
> `c₁(𝒩) ∩ div_ℒ(s) = ∑_i ord_{Z_i,ℒ}(s) · (Z_i → X)_* div_{𝒩|Z_i}(t_i|Z_i)`
>
> in `Z_{n-2}(X)`, where the component cycle at an integral closed subspace `W ⊆ X` is the Weil
> divisor `div_{𝒩|_W}(t_W)` of Stacks 0EQE part (1) on `W` **of a meromorphic section `t_W` this
> statement constructs**: `AlgebraicGeometry.Space.componentMeromorphicSection`, a regular
> meromorphic section of `𝒩|_W` produced by Stacks 0EPQ on `W`, whose hypotheses (a), (b), (c) of
> Stacks 0ENA hold because `W` is integral and locally Noetherian.  The source's `t_i|Z_i` — the
> reduction of a chosen generator of `𝒩_{ξ_i}`,
> `AlgebraicGeometry.Space.PrimeDivisor.genericFibreReduction` — is one such section, and the
> identity holds for any of them: the component cycle is a parameter of Stacks 0EQJ occurring on
> both of its sides.
>
> The dimension function of Stacks 0EDN on each `W` is likewise no longer carried: it is
> `AlgebraicGeometry.Space.subspaceDeltaDimensionFunction`, the dimension function `d` on `|X|`
> pulled back along the closed embedding `|W| → |X|`, which is a dimension function because an
> intermediate point of a specialization starting in a closed set lies in that closed set.
>
> Invertibility of `𝒩` is Section 0EQU's own hypothesis on `𝒩`.  What is still carried on each
> `W` is the pair Stacks 0EQE carries on `X`: the ratio family `ratioN` of Stacks 0EPR and the
> local finiteness `hfinN` of the prime divisors of `W` along which `t_W` has nonzero order,
> Stacks 0EPS.  Neither can be discharged while
> `AlgebraicGeometry.Space.LocalRatio` is an unconstrained function type — a ratio family not
> required to be `s ↦ s / s_ξ` for a generator `s_ξ` makes `ord` arbitrary, so the set of prime
> divisors of nonzero order is not controlled; the *first* set of Stacks 0EPS, which does not
> mention the ratio, is proved and applies to `t_W` because `t_W` is regular, by
> `AlgebraicGeometry.Space.locallyFinite_primeDivisor_not_memGenericModuleStalk_of_isIntegral`.
>
> The key formula itself, Stacks 0EQV, **is** proved, unconditionally and axiom-clean:
> `AlgebraicGeometry.Space.keyFormula_of_ne_zero` of
> `StacksFrontier.AlgebraicGeometry.Spaces.Chow.KeyFormulaProof.Headline`, at the canonical choices and
> for the constructed tame-symbol sum, from which Stacks 0EQX follows there as
> `AlgebraicGeometry.Space.canonicalFirstChernCap_divisor_comm`.  What is still open is only the
> *predicate* `AlgebraicGeometry.Space.KeyFormula` of
> `StacksFrontier.AlgebraicGeometry.Spaces.Chow.KeyFormulaCycleIdentities`, which quantifies the
> component rules of Stacks 0EQJ and the principal divisors of the tame symbols; at that generality
> it is not a theorem of this library.

```lean
theorem firstChernCapCycleMap_divisorCycleAt_eq_componentDivisorSum_of_isInvertible
    {k : ℤ} {I : Type v}
    (hN : IsInvertibleModule (⟨X, hX.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) N)
    (ratioN : ∀ W : IntegralClosedSubspace D.site D.base D.base_mem X,
      LocalRatioFamily.{u, u} D.site D.base D.base_mem (setup.isSpace W) (setup.isDecent W)
        (integralClosedSubspaceRestrict D sX hX N W))
    (d : DimensionFunction (points D.site D.base D.base_mem X))
    (hd : ∀ x, d x = D.deltaValue sX x)
    (hfinN : ∀ W : IntegralClosedSubspace D.site D.base D.base_mem X,
      LocallyFinite fun P : PrimeDivisor D.site D.base D.base_mem W.subspace.toFunctor =>
        if setup.sectionOrder W (integralClosedSubspaceRestrict D sX hX N W)
            (componentMeromorphicSection sX hX setup N hN W) (ratioN W) P = 0
          then ∅ else P.support D.site D.base D.base_mem W.subspace.toFunctor)
    (s : MeromorphicSection.{u, z} D.site D.base D.base_mem X hX.1 L)
    (ratio : LocalRatioFamily.{u, z} D.site D.base D.base_mem hX.1 hdec L)
    (hfin : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem X =>
      if divisorCoefficients.{u, z} D.site D.base D.base_mem hX.1 hdec L s ratio W = 0 then ∅
      else W.support D.site D.base D.base_mem X)
    (hint : IsIntegralSpace D.site D.base D.base_mem X) {n : ℤ}
    (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt))
    (hk : k + 1 = n - 1)
    (Z : I → PrimeDivisor D.site D.base D.base_mem X)
    (hZinj : Function.Injective Z)
    (hZfin : LocallyFinite fun i : I =>
      subspacePointSet D.site D.base D.base_mem X (Z i).subspace)
    (hdim : ∀ i, deltaDimension D sX
      ((Z i).toIntegralClosedSubspace D.site D.base D.base_mem) = k + 1)
    (hcover : ∀ W : PrimeDivisor D.site D.base D.base_mem X,
      divisorCoefficients.{u, z} D.site D.base D.base_mem hX.1 hdec L s ratio W ≠ 0 →
        ∃ i, Z i = W) :
    firstChernCapCycleMap D sX hX k
        (componentDivisorCycleRule sX hX setup N k
          (componentMeromorphicSection sX hX setup N hN) ratioN
          (fun W => subspaceDeltaDimensionFunction D sX hX d W)
          (fun W => subspaceDeltaDimensionFunction_eq_deltaValue D sX hX d hd W) hfinN)
        (divisorCycleAt.{u, z} D sX hX hdec L s ratio hfin hint d hd hn hk) =
      cycleFamilySum D sX hX
        (fun i => (Z i).toIntegralClosedSubspace D.site D.base D.base_mem) hZfin k
        (fun i => orderOfVanishingSection.{u, z} D.site D.base D.base_mem hX.1 hdec (Z i) L s
          (ratio (Z i)) •
            componentDivisorCycleRule sX hX setup N k
              (componentMeromorphicSection sX hX setup N hN) ratioN
              (fun W => subspaceDeltaDimensionFunction D sX hX d W)
              (fun W => subspaceDeltaDimensionFunction_eq_deltaValue D sX hX d hd W) hfinN
              ((Z i).toIntegralClosedSubspace D.site D.base D.base_mem) (hdim i))
```

**`AlgebraicGeometry.Space.canonicalFirstChernCap_divisor_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormulaProof/Headline.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormulaProof/Headline.lean#L137). The attribute's comment: “the key formula of the section, c\_1(N) ∩ div\_L(s) = c\_1(L) ∩ div\_N(t) in CH\_\{n-2}(X), at the section's hypotheses; Lemma 0EQV is keyFormula\_of\_ne\_zero”.

> **Section 0EQU, the key formula: `c₁(𝒩) ∩ div_ℒ(s) = c₁(ℒ) ∩ div_𝒩(t)` in `CH_{n-2}(X)`.**
> In Situation 0EDT let `X/B` be good, `X` integral with `dim_δ(X) = n`, let `ℒ` and `𝒩` be
> invertible `𝒪_X`-modules, and let `s`, `t` be nonzero meromorphic sections of `ℒ`, `𝒩`.  Then
> `c₁(𝒩) ∩ div_ℒ(s) = c₁(ℒ) ∩ div_𝒩(t)` in the Chow group `CH_{n-2}(X)` of Stacks 0EQ6, the cap
> products being those of Stacks 0EQJ and the divisors those of Stacks 0EQE, all at the canonical
> choices.
>
> The proof is the section's: the family `{Z_i}` of prime divisors where `s` or `t` fails to
> generate is locally finite (Stacks 0EPS), the two cap products are the sums over it of
> `ord_{B_i}(f_i) (Z_i → X)_* div(t_i|_{Z_i})` and `ord_{B_i}(g_i) (Z_i → X)_* div(s_i|_{Z_i})`, and
> the key formula (Stacks 0EQV) makes their difference a locally finite sum of principal divisors of
> tame symbols on the `Z_i`.

```lean
theorem canonicalFirstChernCap_divisor_comm
    (s : MeromorphicSection.{u, u} D.site D.base D.base_mem X hX.1 L) (hs : s ≠ 0)
    (t : MeromorphicSection.{u, u} D.site D.base D.base_mem X hX.1 N) (ht : t ≠ 0)
    {n : ℤ} (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt)) :
    canonicalFirstChernCap.{u, u + 1} D sX hX N hN (n - 2)
        (canonicalDivisorCycleAt D sX hX hint L hL s
          (isRegularMeromorphicSection_of_ne_zero_of_isGood D sX hX hint L hL hs)
          (deltaDimensionClosed_eq_sub_two_add_one_add_one D sX hX hn)) =
      canonicalFirstChernCap.{u, u + 1} D sX hX L hL (n - 2)
        (canonicalDivisorCycleAt D sX hX hint N hN t
          (isRegularMeromorphicSection_of_ne_zero_of_isGood D sX hX hint N hN ht)
          (deltaDimensionClosed_eq_sub_two_add_one_add_one D sX hX hn))
```

**`AlgebraicGeometry.Space.canonicalFirstChernCap_canonicalDivisorCycleAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormulaSection.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormulaSection.lean#L309). The attribute's comment: “the cycle identities of the section, in CH\_\{n-2}(X) as the source states them: c\_1(N) ∩ div\_L(s) = ∑ ord\_\{B\_i}(f\_i) (Z\_i → X)\_* div\_\{N|Z\_i}(t\_i|Z\_i), with everything at the canonical choices (the cap product, the divisors and the ratios s = f\_i s\_i are constructed, not carried) and for an arbitrary regular meromorphic section of N|Z\_i in place of t\_i|Z\_i; the second identity is the same statement with (L, s) and (N, t) exchanged. Claims (1)-(2) of the section are canonicalDivisorCycle\_apply\_eq\_zero\_of\_notMem, canonicalDivisorCycle\_apply\_primeDivisor and orderOfVanishingSection\_canonical\_eq\_ord”.

> **Section 0EQU, claim (3).** In Situation 0EDT let `X/B` be good, `X` integral with
> `dim_δ(X) = n = k + 2`, let `ℒ`, `𝒩` be invertible with `s` a regular meromorphic section of
> `ℒ`, and let `{Z_i}` be a locally finite family of prime divisors such that `s` generates `ℒ_ξ`
> at the generic point of every prime divisor outside it.  For generators `s_i = v_i s_{ξ_i}` of
> `ℒ_{ξ_i}` write `s = f_i s_i`, `f_i ∈ Q(B_i)^*`.  Then for any regular meromorphic sections
> `τ_i` of `𝒩|_{Z_i}` — in particular for the source's `t_i|_{Z_i}` —
>
> `c₁(𝒩) ∩ div_ℒ(s) = ∑ ord_{B_i}(f_i) (Z_i → X)_* div_{𝒩|_{Z_i}}(τ_i)`  in `CH_{n-2}(X)`.
>
> The cap product is the one of Stacks 0EQJ at the canonical choices,
> `AlgebraicGeometry.Space.canonicalFirstChernCap`, the divisors are those of Stacks 0EQE at the
> canonical ratios, and `CH_{n-2}(X)` is the Chow group of Stacks 0EQ6.  The second identity of
> the section is this one with `(ℒ, s)` and `(𝒩, t)` exchanged.

```lean
theorem canonicalFirstChernCap_canonicalDivisorCycleAt
    (N : Modules.{u, u} D.site D.base D.base_mem X hX.1)
    (hN : IsInvertibleModule (⟨X, hX.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) N)
    {I : Type v} (Zf : I → PrimeDivisor D.site D.base D.base_mem X)
    (hinj : Function.Injective Zf)
    (hfin : LocallyFinite fun i : I =>
      subspacePointSet D.site D.base D.base_mem X
        ((Zf i).toIntegralClosedSubspace D.site D.base D.base_mem).subspace)
    (hcov : ∀ W : PrimeDivisor D.site D.base D.base_mem X, (∀ i, Zf i ≠ W) →
      W.SectionGenerates D sX hX hint L hL s)
    {k : ℤ}
    (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = ((k + 1 + 1 : ℤ) : EInt))
    (v : ∀ i, ↥((Zf i).genericHenselianLocalRing D.site D.base D.base_mem hX.1
      (isDecentSpace_of_isGood D sX hX)))
    (hv : ∀ i, IsUnit (v i))
    (f : ∀ i, ((Zf i).genericTotalFractionRing D.site D.base D.base_mem hX.1
      (isDecentSpace_of_isGood D sX hX))ˣ)
    (hf : ∀ i, (f i : (Zf i).genericTotalFractionRing D.site D.base D.base_mem hX.1
        (isDecentSpace_of_isGood D sX hX)) * algebraMap _ _ (v i) =
      (Zf i).canonicalGenericRatio D.site D.base D.base_mem hX.1
        (isDecentSpace_of_isGood D sX hX) L hL hint
        (hasEtaleLocalProperty_isLocallyNoetherian_of_isGood D sX hX) s)
    (τ : ∀ i, MeromorphicSection.{u, u} D.site D.base D.base_mem
      ((Zf i).toIntegralClosedSubspace D.site D.base D.base_mem).subspace.toFunctor
      (isGood_integralClosedSubspace D sX hX _).1
      (integralClosedSubspaceRestrict D sX hX N
        ((Zf i).toIntegralClosedSubspace D.site D.base D.base_mem)))
    (hτ : ∀ i, IsRegularMeromorphicSection.{u, u} D.site D.base D.base_mem _
      (isGood_integralClosedSubspace D sX hX _).1 _ (τ i)) :
    haveI := fun W : PrimeDivisor D.site D.base D.base_mem X =>
      W.nontrivial_genericHenselianLocalRing D.site D.base D.base_mem hX.1
        (isDecentSpace_of_isGood D sX hX) hint
        (hasEtaleLocalProperty_isLocallyNoetherian_of_isGood D sX hX)
    haveI := fun W : PrimeDivisor D.site D.base D.base_mem X =>
      W.isNoetherianRing_genericHenselianLocalRing D.site D.base D.base_mem hX.1
        (isDecentSpace_of_isGood D sX hX) hint
        (hasEtaleLocalProperty_isLocallyNoetherian_of_isGood D sX hX)
    haveI := fun W : PrimeDivisor D.site D.base D.base_mem X =>
      W.krullDimLE_genericHenselianLocalRing D.site D.base D.base_mem hX.1
        (isDecentSpace_of_isGood D sX hX) hint
        (hasEtaleLocalProperty_isLocallyNoetherian_of_isGood D sX hX)
    canonicalFirstChernCap.{u, v} D sX hX N hN k
        (canonicalDivisorCycleAt D sX hX hint L hL s hs hn) =
      chowClass.{v} D sX hX k (cycleFamilySum D sX hX
        (fun i => (Zf i).toIntegralClosedSubspace D.site D.base D.base_mem) hfin k
        (fun i => (Zf i).ord D.site D.base D.base_mem hX.1 (isDecentSpace_of_isGood D sX hX)
            (f i : (Zf i).genericTotalFractionRing D.site D.base D.base_mem hX.1
              (isDecentSpace_of_isGood D sX hX)) (f i).isUnit •
          canonicalDivisorCycleAt D _ (isGood_integralClosedSubspace D sX hX _)
            ((Zf i).toIntegralClosedSubspace D.site D.base D.base_mem).isIntegralSpace
            (integralClosedSubspaceRestrict D sX hX N
              ((Zf i).toIntegralClosedSubspace D.site D.base D.base_mem))
            (isInvertibleModule_integralClosedSubspaceRestrict D sX hX N hN _) (τ i) (hτ i)
            (deltaDimensionClosed_univ_toIntegralClosedSubspace D sX hX hint hn (Zf i))))
```

**`AlgebraicGeometry.Space.locallyFinite_primeDivisor_not_sectionGenerates`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormulaSection.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormulaSection.lean#L436). The attribute's comment: “existence of the family \{Z\_i}: the prime divisors at whose generic point s or t fails to generate form a locally finite family (by 0EPS)”.

> **Section 0EQU: the family exists** ("Such a set exists by Spaces over Fields, Lemma 0EPS").
> The prime divisors at whose generic point `s` fails to generate `ℒ_ξ` or `t` fails to generate
> `𝒩_ξ` form a locally finite family; it is the smallest family the section may be taken over.

```lean
theorem locallyFinite_primeDivisor_not_sectionGenerates :
    LocallyFinite fun W : {W : PrimeDivisor D.site D.base D.base_mem X //
        ¬ (W.SectionGenerates D sX hX hint L hL s ∧ W.SectionGenerates D sX hX hint N hN t)} =>
      W.1.support D.site D.base D.base_mem X
```

## Tag 0EQV, a lemma

[Tag 0EQV](https://stacks.math.columbia.edu/tag/0EQV) in the Stacks Project.

**`AlgebraicGeometry.Space.firstChernCapCycleMap_divisorCycleAt_eq_cycleFamilySum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormulaCycleIdentities.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormulaCycleIdentities.lean#L345). The attribute's comment: “the situation above, not the lemma: either cycle identity of Section 0EQU, c\_1(N) ∩ div\_L(s) = ∑ ord\_\{B\_i}(f\_i) (Z\_i → X)\_* div\_\{N|Z\_i}(t\_i|Z\_i) in Z\_\{n-2}(X), for an arbitrary component rule chern of Stacks 0EQJ, of which it uses no property; hdim is Stacks 0EPZ. DISCHARGED ELSEWHERE: the instance at the registered cap product — the component cycle canonicalFirstChernRule at the canonical choices, in CH\_\{n-2}(X) — is canonicalFirstChernCap\_canonicalDivisorCycleAt, and the key formula itself is proved unconditionally as keyFormula\_of\_ne\_zero; neither carries a free component rule”.

> **Either cycle identity of the section preceding the key formula, for an arbitrary component
> rule.**  In Situation 0EDT let `X/B` be good and integral with `dim_δ(X) = n`, let `ℒ` be an
> `𝒪_X`-module with a nonzero meromorphic section `s`, and let `{Z_i}`, `i ∈ I`, be an injective
> locally finite family of prime divisors of `X` containing every prime divisor along which `s` has
> nonzero order of vanishing.  Then
>
> `c₁(𝒩) ∩ div_ℒ(s) = ∑_i ord_{Z_i,ℒ}(s) · (Z_i → X)_*(c₁(𝒩|_{Z_i}) ∩ [Z_i])`
>
> in `Z_{n-2}(X)`.  The two identities displayed in Section 0EQU before the key formula are the two
> instances of this statement: the first is the one above, and the second is obtained by exchanging
> `(ℒ, s)` with `(𝒩, t)` and `𝒩` with `ℒ`, that is by using the component rule of `ℒ` and the
> divisor of `t`.
>
> The orders `ord_{Z_i,ℒ}(s)` are those of Stacks 0EPR, which the source identifies with its
> `ord_{B_i}(f_i)`, and they depend on the `ratio` parameter of Stacks 0EPR only through its value
> at the generic points, not at all by
> `AlgebraicGeometry.Space.orderOfVanishingSection_unit_smul`.  The δ-dimension hypothesis `hdim` is
> Stacks 0EPZ, proved as
> `AlgebraicGeometry.Space.deltaDimension_toIntegralClosedSubspace`.
>
> The component cycle `c₁(𝒩|_{Z_i}) ∩ [Z_i]`, which the source writes `div_{𝒩|Z_i}(t_i|Z_i)`, is
> here the arbitrary component rule `chern` of Stacks 0EQJ: nothing below uses any property of it.
> `AlgebraicGeometry.Space.firstChernCapCycleMap_divisorCycleAt_eq_componentDivisorSum` of
> `StacksFrontier.AlgebraicGeometry.Spaces.Chow.KeyFormulaComponentDivisor` is the instance of this
> statement in which that cycle is the Weil divisor `div_{𝒩|Z_i}(t_i|Z_i)` of Stacks 0EQE part (1)
> on `Z_i`; that is the form Section 0EQU displays, and it carries the tag.
>
> The key formula itself, Stacks 0EQV, **is** proved, at the canonical choices and for the
> constructed tame-symbol sum:
> `AlgebraicGeometry.Space.keyFormula_of_ne_zero` of
> `StacksFrontier.AlgebraicGeometry.Spaces.Chow.KeyFormulaProof.Headline`, from which Section 0EQU's
> `c₁(𝒩) ∩ div_ℒ(s) = c₁(ℒ) ∩ div_𝒩(t)` in `CH_{n-2}(X)` follows as
> `AlgebraicGeometry.Space.canonicalFirstChernCap_divisor_comm`.  What is left open is only the
> predicate `AlgebraicGeometry.Space.KeyFormula` below, which quantifies the component rules and
> the tame-symbol divisors and so cannot be discharged at that generality.

```lean
theorem firstChernCapCycleMap_divisorCycleAt_eq_cycleFamilySum
    {k : ℤ} (chern : FirstChernComponentCycleRule D sX k) {I : Type v}
    (s : MeromorphicSection.{u, z} D.site D.base D.base_mem X hX.1 L)
    (ratio : LocalRatioFamily.{u, z} D.site D.base D.base_mem hX.1 hdec L)
    (hfin : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem X =>
      if divisorCoefficients.{u, z} D.site D.base D.base_mem hX.1 hdec L s ratio W = 0 then ∅
      else W.support D.site D.base D.base_mem X)
    (hint : IsIntegralSpace D.site D.base D.base_mem X)
    (d : DimensionFunction (points D.site D.base D.base_mem X))
    (hd : ∀ x, d x = D.deltaValue sX x) {n : ℤ}
    (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt))
    (hk : k + 1 = n - 1)
    (Z : I → PrimeDivisor D.site D.base D.base_mem X)
    (hZinj : Function.Injective Z)
    (hZfin : LocallyFinite fun i : I =>
      subspacePointSet D.site D.base D.base_mem X (Z i).subspace)
    (hdim : ∀ i, deltaDimension D sX
      ((Z i).toIntegralClosedSubspace D.site D.base D.base_mem) = k + 1)
    (hcover : ∀ W : PrimeDivisor D.site D.base D.base_mem X,
      divisorCoefficients.{u, z} D.site D.base D.base_mem hX.1 hdec L s ratio W ≠ 0 →
        ∃ i, Z i = W) :
    firstChernCapCycleMap D sX hX k chern
        (divisorCycleAt.{u, z} D sX hX hdec L s ratio hfin hint d hd hn hk) =
      cycleFamilySum D sX hX
        (fun i => (Z i).toIntegralClosedSubspace D.site D.base D.base_mem) hZfin k
        (fun i => orderOfVanishingSection.{u, z} D.site D.base D.base_mem hX.1 hdec (Z i) L s
          (ratio (Z i)) •
            chern ((Z i).toIntegralClosedSubspace D.site D.base D.base_mem) (hdim i))
```

**`AlgebraicGeometry.Space.firstChernCap_sub_firstChernCap_eq_cycleFamilySum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormulaCycleIdentities.lean, line 528](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormulaCycleIdentities.lean#L528). The attribute's comment: “the situation above, not the lemma: the FIRST cycle of the key formula equals c\_1(N) ∩ div\_L(s) - c\_1(L) ∩ div\_N(t), from the two cycle identities of Section 0EQU, for arbitrary component rules chernN and chernL of Stacks 0EQJ, of which no property is used; hdim is Stacks 0EPZ. DISCHARGED ELSEWHERE: the key formula itself is proved unconditionally, at the canonical choices and for the constructed tame-symbol sum, as keyFormula\_of\_ne\_zero, and its Section 0EQU consequence in CH\_\{n-2}(X) as canonicalFirstChernCap\_divisor\_comm”.

> The first cycle of the key formula is the difference of the two cap products of Section
> 0EQU: with the family `{Z_i}` containing every prime divisor along which `s` or `t` has nonzero
> order of vanishing,
>
> `c₁(𝒩) ∩ div\_ℒ(s) - c₁(ℒ) ∩ div\_𝒩(t)
>   = ∑\_i (Z\_i → X)\_*(ord\_\{B\_i}(f\_i) div\_\{𝒩|Z\_i}(t\_i|Z\_i) - ord\_\{B\_i}(g\_i) div\_\{ℒ|Z\_i}(s\_i|Z\_i))`
>
> in `Z_{n-2}(X)`.  It is the two cycle identities of Section 0EQU together with additivity of the
> locally finite sum of Stacks 0EQ6 part (1).
>
> The two restricted divisors `div_{𝒩|Z_i}(t_i|Z_i)` and `div_{ℒ|Z_i}(s_i|Z_i)` are the component
> cycles carried as the parameters `chernN` and `chernL` of Stacks 0EQJ, standing in for Stacks 0EQE
> on `Z_i`; the two orders are those of Stacks 0EPR, which the source identifies with
> `ord_{B_i}(f_i)` and `ord_{B_i}(g_i)`; the δ-dimension hypothesis `hdim` is Stacks 0EPZ, proved as
> `AlgebraicGeometry.Space.deltaDimension_toIntegralClosedSubspace`.
>
> The key formula itself — the equality of this cycle with `∑_i (Z_i → X)_* div(∂_{B_i}(f_i, g_i))`
> — **is** proved at the canonical choices, as
> `AlgebraicGeometry.Space.keyFormula_of_ne_zero`; only the predicate
> `AlgebraicGeometry.Space.KeyFormula`, which quantifies the component rules and the tame-symbol
> divisors, is left open.

```lean
theorem firstChernCap_sub_firstChernCap_eq_cycleFamilySum
    (s : MeromorphicSection.{u, z} D.site D.base D.base_mem X hX.1 L)
    (t : MeromorphicSection.{u, z} D.site D.base D.base_mem X hX.1 N)
    (ratioL : LocalRatioFamily.{u, z} D.site D.base D.base_mem hX.1 hdec L)
    (ratioN : LocalRatioFamily.{u, z} D.site D.base D.base_mem hX.1 hdec N)
    (hfinL : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem X =>
      if divisorCoefficients.{u, z} D.site D.base D.base_mem hX.1 hdec L s ratioL W = 0 then ∅
      else W.support D.site D.base D.base_mem X)
    (hfinN : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem X =>
      if divisorCoefficients.{u, z} D.site D.base D.base_mem hX.1 hdec N t ratioN W = 0 then ∅
      else W.support D.site D.base D.base_mem X)
    (hint : IsIntegralSpace D.site D.base D.base_mem X)
    (dim : DimensionFunction (points D.site D.base D.base_mem X))
    (hd : ∀ x, dim x = D.deltaValue sX x) {n : ℤ}
    (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt))
    (hk : k + 1 = n - 1)
    (hZinj : Function.Injective Z)
    (hZfin : LocallyFinite fun i : I =>
      subspacePointSet D.site D.base D.base_mem X (Z i).subspace)
    (hdim : ∀ i, deltaDimension D sX
      ((Z i).toIntegralClosedSubspace D.site D.base D.base_mem) = k + 1)
    (hcoverL : ∀ W : PrimeDivisor D.site D.base D.base_mem X,
      divisorCoefficients.{u, z} D.site D.base D.base_mem hX.1 hdec L s ratioL W ≠ 0 →
        ∃ i, Z i = W)
    (hcoverN : ∀ W : PrimeDivisor D.site D.base D.base_mem X,
      divisorCoefficients.{u, z} D.site D.base D.base_mem hX.1 hdec N t ratioN W ≠ 0 →
        ∃ i, Z i = W) :
    firstChernCapCycleMap D sX hX k chernN
        (divisorCycleAt.{u, z} D sX hX hdec L s ratioL hfinL hint dim hd hn hk) -
      firstChernCapCycleMap D sX hX k chernL
        (divisorCycleAt.{u, z} D sX hX hdec N t ratioN hfinN hint dim hd hn hk) =
      cycleFamilySum D sX hX
        (fun i => (Z i).toIntegralClosedSubspace D.site D.base D.base_mem) hZfin k
        (keyFormulaDivisorTerm.{u, z} D sX hX hdec L N chernL chernN Z s t ratioL ratioN hdim)
```

**`AlgebraicGeometry.Space.keyFormula_of_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormulaProof/Headline.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/KeyFormulaProof/Headline.lean#L93).

> **Stacks 0EQV, the key formula, for nonzero meromorphic sections.** In Situation 0EDT let
> `X/B` be good, `X` integral with `dim_δ(X) = n`, let `ℒ`, `𝒩` be invertible with nonzero
> meromorphic sections `s`, `t`, let `{Z_i}` be an injective locally finite family of prime divisors
> outside of which `s` generates `ℒ_ξ` and `t` generates `𝒩_ξ`, and let `s_i = v_i s_{ξ_i}`,
> `t_i = w_i t_{ξ_i}` be generators of `ℒ_{ξ_i}`, `𝒩_{ξ_i}` (`v_i`, `w_i` units of
> `B_i = 𝒪^h_{X,ξ_i}`; every generator is of this form for a unique unit), so that `s = f_i s_i`,
> `t = g_i t_i` with `f_i, g_i ∈ Q(B_i)^*`.  Then
>
> `∑ (Z\_i → X)\_*(ord\_\{B\_i}(f\_i) div\_\{𝒩|\_\{Z\_i}}(t\_i|\_\{Z\_i})
>     - ord\_\{B\_i}(g\_i) div\_\{ℒ|\_\{Z\_i}}(s\_i|\_\{Z\_i}))
>   = ∑ (Z\_i → X)\_* div(∂\_\{B\_i}(f\_i, g\_i))`
>
> in `Z_{n-2}(X)`, with `t_i|_{Z_i}` the image of `t_i` in the fibre `𝒩_{ξ_i} ⊗ κ(ξ_i)` read as a
> meromorphic section of `𝒩|_{Z_i}`, and `∂_{B_i}` the tame symbol of Stacks 0EAH read in
> `κ(ξ_i)^* = R(Z_i)^*`.

```lean
theorem keyFormula_of_ne_zero
    (s : MeromorphicSection.{u, u} D.site D.base D.base_mem X hX.1 L) (hs : s ≠ 0)
    (t : MeromorphicSection.{u, u} D.site D.base D.base_mem X hX.1 N) (ht : t ≠ 0)
    {n : ℤ} (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt))
    {I : Type*} (Zf : I → PrimeDivisor D.site D.base D.base_mem X)
    (hfin : LocallyFinite fun i : I =>
      subspacePointSet D.site D.base D.base_mem X
        ((Zf i).toIntegralClosedSubspace D.site D.base D.base_mem).subspace)
    (hinj : Function.Injective Zf)
    (hcov : ∀ W : PrimeDivisor D.site D.base D.base_mem X, (∀ i, Zf i ≠ W) →
      W.SectionGenerates D sX hX hint L hL s ∧ W.SectionGenerates D sX hX hint N hN t)
    (v w : ∀ i, (↥((Zf i).genericHenselianLocalRing D.site D.base D.base_mem hX.1
      (isDecentSpace_of_isGood D sX hX)))ˣ) :
    keyFormulaDivisorSum D sX hX hint L hL s
        (isRegularMeromorphicSection_of_ne_zero_of_isGood D sX hX hint L hL hs) N hN t
        (isRegularMeromorphicSection_of_ne_zero_of_isGood D sX hX hint N hN ht)
        (deltaDimensionClosed_eq_sub_two_add_one_add_one D sX hX hn) Zf hfin v w =
      keyFormulaTameSum D sX hX hint L hL s
        (isRegularMeromorphicSection_of_ne_zero_of_isGood D sX hX hint L hL hs) N hN t
        (isRegularMeromorphicSection_of_ne_zero_of_isGood D sX hX hint N hN ht)
        (deltaDimensionClosed_eq_sub_two_add_one_add_one D sX hX hn) Zf hfin v w
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.20, Tag 0EQU](https://stacks.math.columbia.edu/tag/0EQU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
