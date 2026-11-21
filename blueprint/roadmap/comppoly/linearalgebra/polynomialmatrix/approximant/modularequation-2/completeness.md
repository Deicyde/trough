---
catalog: module
lean: CompPoly.PolynomialMatrix.Approximant.me_getD_mem_toList, CompPoly.PolynomialMatrix.Approximant.me_rowShiftedDegree_isSome, CompPoly.PolynomialMatrix.Approximant.me_filterModularSolutionRows_subset, CompPoly.PolynomialMatrix.Approximant.me_principalSolutionRows_width, CompPoly.PolynomialMatrix.Approximant.me_adaptiveBasis_width, CompPoly.PolynomialMatrix.Approximant.me_prodRow_facts, CompPoly.PolynomialMatrix.Approximant.me_verification_dominates
statement: formalized
proof: formalized
---

# Filtered Modular Solver Completeness

`CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.ModularEquation.Completeness`, in [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Completeness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Completeness.lean), by Valerii Huhnin.

> Completeness/minimality of the filtered PM-basis modular solver: every
> nonzero in-width solution of a monic diagonal modular equation is dominated
> by a returned row, via the certified verification window.

> ## Completeness/minimality of the filtered PM-basis modular solver
>
> The argument routes every modular solution through the certified verification
> window.  A nonzero in-width solution row of shifted degree `e ≤ bound` lifts
> to an exact row of the reduced exact-nullspace problem whose expanded shifted
> degree is at most `e + bound + 1`.  The PM-basis minimality contract yields a
> basis row of dominated expanded degree, the verification orders force its
> column products to vanish exactly, and its principal truncation is therefore a
> modular solution of shifted degree at most `e` surviving both filters.
> Solutions above the verification window are handled either by the adaptive
> rows themselves or by falling back to the always-available solution
> `e_p * prod(moduli)`, which fits the saturated window.

> ### Generic access and summation helpers

`CompPoly.PolynomialMatrix.Approximant.me_getD_mem_toList` (theorem, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Completeness.lean#L77))

> In-bounds `getD` values are list members.

```lean
theorem me_getD_mem_toList {α : Type*} {xs : Array α} {i : Nat} (d : α)
    (hi : i < xs.size) : xs.getD i d ∈ xs.toList
```

> ### Zero-row and shifted-degree helpers

`CompPoly.PolynomialMatrix.Approximant.me_rowShiftedDegree_isSome` (theorem, [line 183](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Completeness.lean#L183))

> Nonzero rows have a shifted degree.

```lean
theorem me_rowShiftedDegree_isSome {row : PolynomialRow F} {shift : Array Nat}
    (hnz : rowIsZero row = false) :
    ∃ d, rowShiftedDegree? row shift = some d
```

> ### `maxShiftDegree` and modulus-product bounds

> ### Modular-reduction semantics (local copies of the GS bridge lemmas)

> ### Membership plumbing for the pipeline filters

`CompPoly.PolynomialMatrix.Approximant.me_filterModularSolutionRows_subset` (theorem, [line 414](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Completeness.lean#L414))

> Filtered modular-solution rows come from the input rows.

```lean
theorem me_filterModularSolutionRows_subset
    {mulCtx : CPolynomial.MulContext F} {modCtx : CPolynomial.ModContext F}
    {equation : ModularEquation F} {rows : PolynomialMatrix F}
    {row : PolynomialRow F}
    (hrow : row ∈ MatrixRows (filterModularSolutionRows mulCtx modCtx equation rows)) :
    row ∈ MatrixRows rows
```

`CompPoly.PolynomialMatrix.Approximant.me_principalSolutionRows_width` (theorem, [line 462](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Completeness.lean#L462))

> Principal solution rows keep the basis row width.

```lean
theorem me_principalSolutionRows_width {sW : Nat}
    {basis : PolynomialMatrix F} {row : PolynomialRow F}
    (hrow : row ∈ MatrixRows (principalSolutionRows sW basis)) :
    row.size = sW
```

> ### Width discipline of the adaptive pipeline

`CompPoly.PolynomialMatrix.Approximant.me_adaptiveBasis_width` (theorem, [line 537](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Completeness.lean#L537))

> Every adaptive solution-basis row has the linearized width.

```lean
theorem me_adaptiveBasis_width
    {mulCtx : CPolynomial.MulContext F} {modCtx : CPolynomial.ModContext F}
    {pmCtx : PMBasisContext F} {equation : ModularEquation F}
    {shift : Array Nat} {degreeBound? : Option Nat} :
    ∀ r ∈ MatrixRows
        (adaptiveSolutionBasis mulCtx modCtx pmCtx equation shift
          degreeBound?).filtered,
      r.size = equation.solutionWidth
```

> ### The fallback solution `e_p * prod(moduli)`

`CompPoly.PolynomialMatrix.Approximant.me_prodRow_facts` (theorem, [line 551](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Completeness.lean#L551))

> Structure of the fallback row `e_p * prod(moduli)`.

```lean
theorem me_prodRow_facts (mulCtx : CPolynomial.MulContext F)
    (modCtx : CPolynomial.ModContext F) (equation : ModularEquation F)
    (shift : Array Nat) {p : Nat}
    (hmonic : ∀ b, b < equation.moduli.size → (equation.moduli.getD b 0).monic)
    (hcols : equation.moduli.size ≤ MatrixWidth equation.matrix)
    (hp : p < equation.solutionWidth) :
    ∃ (prow : PolynomialRow F) (e : Nat),
      rowSatisfiesModularBool mulCtx modCtx prow equation.matrix
        equation.moduli = true ∧
      rowIsZero prow = false ∧
      prow.size = equation.solutionWidth ∧
      rowShiftedDegree? prow shift = some e ∧
      e ≤ pivotWindowCap equation + maxShiftDegree shift
```

> ### The certified verification window

`CompPoly.PolynomialMatrix.Approximant.me_verification_dominates` (theorem, [line 614](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Completeness.lean#L614))

> Certified-window domination: any nonzero in-width modular solution row
> whose shifted degree fits inside the verification window `bound` is
> degree-dominated by a row of the filtered verification basis.

```lean
theorem me_verification_dominates
    (mulCtx : CPolynomial.MulContext F) (modCtx : CPolynomial.ModContext F)
    (pmCtx : PMBasisContext F) (equation : ModularEquation F)
    (shift : Array Nat) (bound : Nat) {rowStar : PolynomialRow F} {e : Nat}
    (hmonic : ∀ b, b < equation.moduli.size → (equation.moduli.getD b 0).monic)
    (hcols : equation.moduli.size ≤ MatrixWidth equation.matrix)
    (hshift : shift.size = equation.solutionWidth)
    (hpos : 0 < equation.solutionWidth)
    (hsat : rowSatisfiesModularBool mulCtx modCtx rowStar equation.matrix
      equation.moduli = true)
    (hnz : rowIsZero rowStar = false)
    (hwidth : rowStar.size ≤ equation.solutionWidth)
    (hdeg : rowShiftedDegree? rowStar shift = some e)
    (hebound : e ≤ bound) :
    ∃ basisRow degree,
      basisRow ∈ MatrixRows (filterModularSolutionRows mulCtx modCtx equation
        (compactNonzeroRows (principalSolutionRows equation.solutionWidth
          (pmCtx.basis (fullWindowExactNullspaceProblem modCtx equation bound)
            (exactNullspaceShift shift equation.modularWidth bound))))) ∧
      rowShiftedDegree? basisRow shift = some degree ∧ degree ≤ e
```

## Depends on

- [Diagonal Modular Equations](basic.md)

## Proof depends on

- [X-Adic Row Soundness Toolkit](../pmbasis-2/xadicsoundness.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Completeness.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Completeness.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.ModularEquation.Completeness.json)
