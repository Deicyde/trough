---
catalog: module
lean: CompPoly.PolynomialMatrix.Approximant.ModularEquation, CompPoly.PolynomialMatrix.Approximant.ModularEquation.solutionWidth, CompPoly.PolynomialMatrix.Approximant.ModularEquation.modularWidth, CompPoly.PolynomialMatrix.Approximant.negativeDiagonalRows, CompPoly.PolynomialMatrix.Approximant.exactNullspaceLift, CompPoly.PolynomialMatrix.Approximant.principalSolutionRows, CompPoly.PolynomialMatrix.Approximant.exactNullspaceProblem, CompPoly.PolynomialMatrix.Approximant.chunkedLiftOrders, CompPoly.PolynomialMatrix.Approximant.chunkedPrincipalRows, CompPoly.PolynomialMatrix.Approximant.chunkedExactNullspaceLift, CompPoly.PolynomialMatrix.Approximant.chunkedExactNullspaceProblem, CompPoly.PolynomialMatrix.Approximant.chunkedExactNullspaceProblemForShift, CompPoly.PolynomialMatrix.Approximant.PivotDegreeProfile, CompPoly.PolynomialMatrix.Approximant.emptyPivotDegreeProfile, CompPoly.PolynomialMatrix.Approximant.PivotDegreeProfile.insert, CompPoly.PolynomialMatrix.Approximant.PivotDegreeProfile.coversAll, CompPoly.PolynomialMatrix.Approximant.PivotDegreeProfile.discoveredAny, CompPoly.PolynomialMatrix.Approximant.pivotDegreeProfileMergeRows, CompPoly.PolynomialMatrix.Approximant.pivotDegreeProfileFromRows, CompPoly.PolynomialMatrix.Approximant.solutionBasisWithPlanViaPMBasis, CompPoly.PolynomialMatrix.Approximant.solutionBasisViaPMBasis, CompPoly.PolynomialMatrix.Approximant.knownDegreeSolutionBasisViaPMBasis, CompPoly.PolynomialMatrix.Approximant.unchunkedSolutionBasisViaPMBasis, CompPoly.PolynomialMatrix.Approximant.filterModularSolutionRows, CompPoly.PolynomialMatrix.Approximant.modularResidualRows, CompPoly.PolynomialMatrix.Approximant.candidateRowShift, CompPoly.PolynomialMatrix.Approximant.pivotWindowCap, CompPoly.PolynomialMatrix.Approximant.fullWindowDegreeBound, CompPoly.PolynomialMatrix.Approximant.reducedExactNullspaceLift, CompPoly.PolynomialMatrix.Approximant.fullWindowExactNullspaceProblem, CompPoly.PolynomialMatrix.Approximant.fullWindowSolutionBasisViaPMBasis, CompPoly.PolynomialMatrix.Approximant.verificationWindowBound, CompPoly.PolynomialMatrix.Approximant.windowedSolutionBasisViaPMBasis, CompPoly.PolynomialMatrix.Approximant.verificationSolutionBasisViaPMBasis, CompPoly.PolynomialMatrix.Approximant.degreeGatePassed, CompPoly.PolynomialMatrix.Approximant.gatedWindowBound, CompPoly.PolynomialMatrix.Approximant.degreeGatePassed_eq_true_iff, CompPoly.PolynomialMatrix.Approximant.adaptiveProfileDegrees, CompPoly.PolynomialMatrix.Approximant.leastSolutionRowDegree?, CompPoly.PolynomialMatrix.Approximant.coordinateSettled, CompPoly.PolynomialMatrix.Approximant.allCoordinatesSettled, CompPoly.PolynomialMatrix.Approximant.escalateUnsettledBudgets, CompPoly.PolynomialMatrix.Approximant.AdaptiveSolveState, CompPoly.PolynomialMatrix.Approximant.adaptiveSolutionRound, CompPoly.PolynomialMatrix.Approximant.adaptiveSolutionLoop, CompPoly.PolynomialMatrix.Approximant.adaptiveSolutionBasis, CompPoly.PolynomialMatrix.Approximant.discoverPivotDegreeProfileViaPMBasis, CompPoly.PolynomialMatrix.Approximant.repairSolutionRowsViaPMBasis, CompPoly.PolynomialMatrix.Approximant.debugUnchunkedFilteredSolutionBasisViaPMBasis, CompPoly.PolynomialMatrix.Approximant.knownDegreeFilteredSolutionBasisViaPMBasis, CompPoly.PolynomialMatrix.Approximant.filteredSolutionBasisViaPMBasis, CompPoly.PolynomialMatrix.Approximant.rowSatisfiesModularBool_of_mem_filterModularSolutionRows, CompPoly.PolynomialMatrix.Approximant.adaptiveSolutionRound_filtered_sound, CompPoly.PolynomialMatrix.Approximant.adaptiveSolutionLoop_filtered_sound, CompPoly.PolynomialMatrix.Approximant.adaptiveSolutionBasis_filtered_sound, CompPoly.PolynomialMatrix.Approximant.filteredSolutionBasisViaPMBasis_sound, CompPoly.PolynomialMatrix.Approximant.ModularSolutionBasisContext
statement: formalized
proof: formalized
---

# Diagonal Modular Equations

`CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.ModularEquation.Basic`, in [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean), by Valerii Huhnin.

> GS-independent solution-basis interface for systems
> `p * matrix = 0 mod diag(moduli)`.
>
> The production solver follows the degree-first pattern: it solves chunked
> exact-nullspace X-adic problems whose partial-linearization windows are grown
> adaptively per principal coordinate, doubling only the windows of coordinates
> whose shifted pivot degree has not been discovered yet.  Because a window stops
> growing once its coordinate's pivot is found, the total window mass stays
> within a constant factor of the true pivot-degree mass, which is at most the
> modulus degree mass `sigma`.  Every round is therefore an X-adic problem with
> `O(m)` chunk rows and total order `O(sigma)`, and the number of rounds is
> logarithmic, preserving the `~O(m^(omega-1) * sigma)` solver target.
>
> The chunked X-adic problems are relaxations: their orders certify exactness
> only for rows whose chunk coefficients stay below the chunk size, and the
> relaxed kernel module also contains uncertified rows that can crowd exact
> solutions out of the adaptive rounds.  The solver therefore backs the adaptive
> loop with a certified verification solve (`windowedSolutionBasisViaPMBasis`):
> solutions at or above the adaptive best are dominated by the adaptive rows,
> and solutions below it lie inside the certified window, whose orders rule out
> uncertified rows.
>
> Callers that only need a witness under a known degree bound pass it as
> `degreeBound?`; when the adaptive best already meets the bound the certified
> solve is skipped entirely, and when it does not the certified window is shrunk
> to the bound.  Passing `none` requests a degree-minimal answer and always runs
> the verification solve over the best-degree-shrunk window.
>
> ## References
>
> * [Giorgi, P., Jeannerod, C.-P., and Villard, G., *On the complexity of
>     polynomial matrix computations*][GJV03]
> * [Storjohann, A., *Notes on computing minimal approximant bases*][Sto06]
> * [Chowdhury, M. F. I., Jeannerod, C.-P., Neiger, V., Schost, E., and
>     Villard, G., *Faster algorithms for multivariate interpolation with
>     multiplicities and simultaneous polynomial approximations*][CJNSV15]

`CompPoly.PolynomialMatrix.Approximant.ModularEquation` (structure, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L69))

> Diagonal modular-equation data.  Rows of `matrix` are solution coordinates;
> columns are reduced independently by `moduli`.

```lean
structure ModularEquation (F : Type*) [Zero F] where
  moduli : Array (CPolynomial F)
  matrix : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.ModularEquation.solutionWidth` (definition, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L74))

> Number of principal solution coordinates.

```lean
def ModularEquation.solutionWidth (equation : ModularEquation F) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.ModularEquation.modularWidth` (definition, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L78))

> Number of modular columns.

```lean
def ModularEquation.modularWidth (equation : ModularEquation F) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.negativeDiagonalRows` (definition, [line 82](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L82))

> Diagonal rows `-diag(moduli)` for the exact-nullspace lift.

```lean
def negativeDiagonalRows (moduli : Array (CPolynomial F)) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.exactNullspaceLift` (definition, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L87))

> Exact-nullspace lift `[F; -diag(M)]`.

```lean
def exactNullspaceLift (equation : ModularEquation F) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.principalSolutionRows` (definition, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L92))

> Principal solution rows: keep the first `solutionWidth` entries of each
> expanded nullspace row.

```lean
def principalSolutionRows (solutionWidth : Nat) (basis : PolynomialMatrix F) :
    PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.exactNullspaceProblem` (definition, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L99))

> Build the X-adic exact-nullspace problem used by the modular-equation
> solver.

```lean
def exactNullspaceProblem (equation : ModularEquation F) : XAdicProblem F
```

`CompPoly.PolynomialMatrix.Approximant.chunkedLiftOrders` (definition, [line 110](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L110))

> Entry-aware X-adic orders for a chunked exact-nullspace lift.  A balanced
> in-window solution has chunk coefficients of degree below `delta`, and the
> chunked principal entries of column `b` are reduced below `deg M_b`, so
> `delta + maxEntryDeg + 1` low coefficients certify that its principal product
> vanishes exactly.  This is never larger than the generic
> `deg M_b + delta + 1` order and is much smaller when the relation entries have
> low degree.

```lean
def chunkedLiftOrders (delta modularWidth : Nat)
    (chunkedPrincipal : PolynomialMatrix F) : Array Nat
```

`CompPoly.PolynomialMatrix.Approximant.chunkedPrincipalRows` (definition, [line 126](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L126))

> Principal rows for the chunked exact-nullspace lift.  Chunk row
> `(coord, offset)` stores `X^offset` times the corresponding original relation
> row, reduced columnwise by the diagonal moduli.  Reducing keeps every entry of
> column `b` below `deg M_b`, matching the `E * F mod M` expansion from the
> design notes and keeping chunked entry degrees independent of the offsets.

```lean
def chunkedPrincipalRows (modCtx : CPolynomial.ModContext F)
    (equation : ModularEquation F)
    (plan : PartialLinearizationPlan) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.chunkedExactNullspaceLift` (definition, [line 137](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L137))

> Chunked exact-nullspace lift for a partial-linearization plan.

```lean
def chunkedExactNullspaceLift (modCtx : CPolynomial.ModContext F)
    (equation : ModularEquation F)
    (plan : PartialLinearizationPlan) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.chunkedExactNullspaceProblem` (definition, [line 144](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L144))

> Build the X-adic exact-nullspace problem after principal-coordinate chunk
> expansion, with generic partial-linearization orders.

```lean
def chunkedExactNullspaceProblem (modCtx : CPolynomial.ModContext F)
    (equation : ModularEquation F)
    (plan : PartialLinearizationPlan) : XAdicProblem F
```

`CompPoly.PolynomialMatrix.Approximant.chunkedExactNullspaceProblemForShift` (definition, [line 153](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L153))

> Build the chunked X-adic exact-nullspace problem with entry-aware orders.
> The `shift` argument is kept for call-site symmetry; orders depend only on the
> chunked entry degrees and the chunk size.

```lean
def chunkedExactNullspaceProblemForShift (modCtx : CPolynomial.ModContext F)
    (equation : ModularEquation F)
    (plan : PartialLinearizationPlan) (_shift : Array Nat) : XAdicProblem F
```

`CompPoly.PolynomialMatrix.Approximant.PivotDegreeProfile` (structure, [line 163](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L163))

> Shifted pivot-degree profile discovered for the principal solution
> coordinates.  `none` means that the discovery pass did not see a row pivoting in
> that coordinate, so partial linearization uses its conservative fallback.

```lean
structure PivotDegreeProfile where
  degrees : Array (Option Nat)
deriving Repr, BEq
```

`CompPoly.PolynomialMatrix.Approximant.emptyPivotDegreeProfile` (definition, [line 168](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L168))

> Empty shifted pivot-degree profile for a fixed principal width.

```lean
def emptyPivotDegreeProfile (solutionWidth : Nat) : PivotDegreeProfile
```

`CompPoly.PolynomialMatrix.Approximant.PivotDegreeProfile.insert` (definition, [line 173](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L173))

> Insert a discovered pivot degree, keeping the smallest degree for each
> principal leading position.

```lean
def PivotDegreeProfile.insert (profile : PivotDegreeProfile)
    (position degree : Nat) : PivotDegreeProfile
```

`CompPoly.PolynomialMatrix.Approximant.PivotDegreeProfile.coversAll` (definition, [line 183](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L183))

> Whether the profile has discovered a pivot degree for every coordinate.

```lean
def PivotDegreeProfile.coversAll (profile : PivotDegreeProfile) : Bool
```

`CompPoly.PolynomialMatrix.Approximant.PivotDegreeProfile.discoveredAny` (definition, [line 187](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L187))

> Whether the profile has discovered a pivot degree for any coordinate.

```lean
def PivotDegreeProfile.discoveredAny (profile : PivotDegreeProfile) : Bool
```

`CompPoly.PolynomialMatrix.Approximant.pivotDegreeProfileMergeRows` (definition, [line 191](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L191))

> Merge the principal pivot degrees observed in `rows` into a profile.

```lean
def pivotDegreeProfileMergeRows (profile : PivotDegreeProfile)
    (solutionWidth : Nat) (rows : PolynomialMatrix F) (shift : Array Nat) :
    PivotDegreeProfile
```

`CompPoly.PolynomialMatrix.Approximant.pivotDegreeProfileFromRows` (definition, [line 207](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L207))

> Discover principal pivot degrees from compressed candidate rows.

```lean
def pivotDegreeProfileFromRows (solutionWidth : Nat)
    (rows : PolynomialMatrix F) (shift : Array Nat) :
    PivotDegreeProfile
```

`CompPoly.PolynomialMatrix.Approximant.solutionBasisWithPlanViaPMBasis` (definition, [line 214](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L214))

> Solve a diagonal modular equation with a supplied partial-linearization plan.

```lean
def solutionBasisWithPlanViaPMBasis (modCtx : CPolynomial.ModContext F)
    (pmCtx : PMBasisContext F)
    (equation : ModularEquation F) (shift : Array Nat)
    (plan : PartialLinearizationPlan) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.solutionBasisViaPMBasis` (definition, [line 226](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L226))

> Solve once with the conservative shift-spread window.  This is a debug
> entry point only: its chunk count can grow quadratically in the module width
> for spread-out shifts, so the production solver uses the adaptive
> window-escalation loop instead.

```lean
def solutionBasisViaPMBasis (modCtx : CPolynomial.ModContext F)
    (pmCtx : PMBasisContext F)
    (equation : ModularEquation F) (shift : Array Nat) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.knownDegreeSolutionBasisViaPMBasis` (definition, [line 236](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L236))

> Known-degree reconstruction pass: build the partial-linearization plan from
> the discovered pivot degrees and solve the X-adic problem directly for that
> profile.

```lean
def knownDegreeSolutionBasisViaPMBasis (modCtx : CPolynomial.ModContext F)
    (pmCtx : PMBasisContext F)
    (equation : ModularEquation F) (shift : Array Nat)
    (profile : PivotDegreeProfile) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.unchunkedSolutionBasisViaPMBasis` (definition, [line 247](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L247))

> Solve once without principal-coordinate chunking.  This is an explicit
> tiny-leaf/debug entry point; the default modular-equation context does not use
> it as a production fallback.

```lean
def unchunkedSolutionBasisViaPMBasis (modCtx : CPolynomial.ModContext F)
    (pmCtx : PMBasisContext F)
    (equation : ModularEquation F) (shift : Array Nat) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.filterModularSolutionRows` (definition, [line 256](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L256))

> Keep only rows that satisfy the original diagonal modular equation after
> compression from the exact-nullspace / X-adic bridge.

```lean
def filterModularSolutionRows
    (mulCtx : CPolynomial.MulContext F) (modCtx : CPolynomial.ModContext F)
    (equation : ModularEquation F) (rows : PolynomialMatrix F) :
    PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.modularResidualRows` (definition, [line 267](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L267))

> Residual rows `B * F mod diag(M)` for candidate solution rows `B`.

```lean
def modularResidualRows
    (mulCtx : CPolynomial.MulContext F) (modCtx : CPolynomial.ModContext F)
    (equation : ModularEquation F) (rows : PolynomialMatrix F) :
    PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.candidateRowShift` (definition, [line 277](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L277))

> Shift used for polynomial combinations of compressed candidate rows.  The
> degree of a coefficient multiplying row `i` is measured relative to the shifted
> degree already carried by that candidate row.

```lean
def candidateRowShift (rows : PolynomialMatrix F) (shift : Array Nat) : Array Nat
```

`CompPoly.PolynomialMatrix.Approximant.pivotWindowCap` (definition, [line 284](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L284))

> Upper bound for the adaptive search window above each coordinate's shift.
> The row `e_j * lcm(moduli)` is always a solution and `deg lcm(moduli)` is at
> most the modulus degree mass, so every coordinate's minimal shifted pivot
> degree is within this window.

```lean
def pivotWindowCap (equation : ModularEquation F) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.fullWindowDegreeBound` (definition, [line 293](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L293))

> Coefficient-degree bound for the full-window fallback problem.  Any row of
> the lifted module whose shifted degree does not exceed the shifted degree of an
> in-window solution has plain coefficient degrees at most
> `pivotWindowCap + maxShiftDegree shift`: comparing two principal coordinates
> costs at most the shift spread, and `pivotWindowCap` bounds every minimal
> pivot degree.

```lean
def fullWindowDegreeBound (equation : ModularEquation F)
    (shift : Array Nat) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.reducedExactNullspaceLift` (definition, [line 300](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L300))

> Exact-nullspace lift with the relation entries reduced columnwise by the
> moduli, so every principal entry of column `b` has degree below `deg M_b` and
> the quotient coefficients of exact solutions stay below the solution degree.

```lean
def reducedExactNullspaceLift (modCtx : CPolynomial.ModContext F)
    (equation : ModularEquation F) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.fullWindowExactNullspaceProblem` (definition, [line 315](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L315))

> Unchunked exact-nullspace problem with orders certifying exactness across
> the whole pivot window: a lifted row with principal coefficient degrees at most
> `bound` and quotient coefficient degrees at most `bound + 1` produces column-`b`
> products of degree below `deg M_b + bound + 2`, so vanishing to that X-adic
> order forces the product to vanish exactly.  Unlike the chunked relaxation,
> this problem admits no uncertified rows below the in-window solution degrees,
> at the cost of an order mass larger by a factor of the module width.

```lean
def fullWindowExactNullspaceProblem (modCtx : CPolynomial.ModContext F)
    (equation : ModularEquation F) (bound : Nat) : XAdicProblem F
```

`CompPoly.PolynomialMatrix.Approximant.fullWindowSolutionBasisViaPMBasis` (definition, [line 326](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L326))

> Certified full-window solve: compute a minimal basis of the unchunked
> exact-nullspace problem whose orders cover the entire pivot window, and keep
> the principal columns.  Every returned row that pivots at or below an in-window
> solution degree is an exact modular solution, so this entry point cannot lose
> the solution basis to uncertified low-degree rows.  It is used as the fallback
> when the chunked adaptive solver discovers nothing.

```lean
def fullWindowSolutionBasisViaPMBasis (modCtx : CPolynomial.ModContext F)
    (pmCtx : PMBasisContext F) (equation : ModularEquation F)
    (shift : Array Nat) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.verificationWindowBound` (definition, [line 341](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L341))

> Certified verification window sized by the best exact degree already in
> hand.  Solutions at or above the best adaptive degree are dominated by the
> adaptive result itself, so the certified window only has to cover the degrees
> strictly below it; when the adaptive loop found nothing it falls back to the
> full pivot window.

```lean
def verificationWindowBound (equation : ModularEquation F)
    (shift : Array Nat) (bestDegree? : Option Nat) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.windowedSolutionBasisViaPMBasis` (definition, [line 352](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L352))

> Certified solve over an explicit coefficient-degree window: an unchunked
> exact-nullspace problem whose orders certify exactness for every row dominated
> by an in-window solution.  Its order mass is `sigma + s * bound` instead of
> the full window's `(s + 1) * sigma`, so when the window is shrunk to a
> near-minimal degree this costs about one extra cheap round.

```lean
def windowedSolutionBasisViaPMBasis (modCtx : CPolynomial.ModContext F)
    (pmCtx : PMBasisContext F) (equation : ModularEquation F)
    (shift : Array Nat) (bound : Nat) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.verificationSolutionBasisViaPMBasis` (definition, [line 362](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L362))

> Certified verification solve over the best-degree-shrunk window sized by
> `verificationWindowBound`.

```lean
def verificationSolutionBasisViaPMBasis (modCtx : CPolynomial.ModContext F)
    (pmCtx : PMBasisContext F) (equation : ModularEquation F)
    (shift : Array Nat) (bestDegree? : Option Nat) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.degreeGatePassed` (definition, [line 373](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L373))

> Whether a caller-supplied degree bound certifies the adaptive result: the
> gate passes when the best exact degree already found does not exceed the
> bound, in which case any solution within the bound is dominated by the
> adaptive rows up to the bound itself and the certified verification solve is
> unnecessary.

```lean
def degreeGatePassed (degreeBound? bestDegree? : Option Nat) : Bool
```

`CompPoly.PolynomialMatrix.Approximant.gatedWindowBound` (definition, [line 382](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L382))

> Verification window for a gated solve.  With a caller-supplied degree
> bound the window only has to cover solutions within the bound, so it is
> `min(bound, cap) + maxShift`; without one it falls back to the best-degree
> window of `verificationWindowBound`.

```lean
def gatedWindowBound (equation : ModularEquation F)
    (shift : Array Nat) (degreeBound? bestDegree? : Option Nat) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.degreeGatePassed_eq_true_iff` (theorem, [line 389](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L389))

> The degree gate passes exactly for a bound certified by an adaptive best.

```lean
theorem degreeGatePassed_eq_true_iff {degreeBound? bestDegree? : Option Nat} :
    degreeGatePassed degreeBound? bestDegree? = true ↔
      ∃ bound best, degreeBound? = some bound ∧ bestDegree? = some best ∧
        best ≤ bound
```

`CompPoly.PolynomialMatrix.Approximant.adaptiveProfileDegrees` (definition, [line 403](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L403))

> Pivot-degree assignment for one adaptive round: discovered coordinates use
> their observed pivot degrees, undiscovered coordinates use the current
> escalation window above their shift entry.

```lean
def adaptiveProfileDegrees (shift : Array Nat) (profile : PivotDegreeProfile)
    (budgets : Array Nat) (solutionWidth : Nat) : Array (Option Nat)
```

`CompPoly.PolynomialMatrix.Approximant.leastSolutionRowDegree?` (definition, [line 412](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L412))

> Least shifted degree among accumulated solution rows.

```lean
def leastSolutionRowDegree? (rows : PolynomialMatrix F) (shift : Array Nat) :
    Option Nat
```

`CompPoly.PolynomialMatrix.Approximant.coordinateSettled` (definition, [line 424](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L424))

> A coordinate needs no wider search window once its pivot degree is
> discovered, its window has reached the cap, or its window already covers every
> degree below the best solution row found so far.  The last rule is what keeps
> the loop from growing windows for coordinates that cannot improve the answer:
> a row pivoting at `j` with shifted degree below the current best would lie
> inside the already-searched window.  Improving on `best` needs a row of degree
> at most `best - 1`, so the window `shift[j] + budget[j]` suffices once
> `best <= shift[j] + budget[j] + 1`.

```lean
def coordinateSettled (profile : PivotDegreeProfile) (budgets : Array Nat)
    (cap : Nat) (bestDegree? : Option Nat) (shift : Array Nat) (j : Nat) : Bool
```

`CompPoly.PolynomialMatrix.Approximant.allCoordinatesSettled` (definition, [line 433](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L433))

> Whether every principal coordinate is settled for the current windows.

```lean
def allCoordinatesSettled (profile : PivotDegreeProfile) (budgets : Array Nat)
    (cap : Nat) (bestDegree? : Option Nat) (shift : Array Nat)
    (solutionWidth : Nat) : Bool
```

`CompPoly.PolynomialMatrix.Approximant.escalateUnsettledBudgets` (definition, [line 442](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L442))

> Double the escalation windows of coordinates that are not settled, clamped
> at the window cap.  Settled coordinates keep their window so the total window
> mass stays within a constant factor of the useful pivot-degree mass.

```lean
def escalateUnsettledBudgets (profile : PivotDegreeProfile)
    (budgets : Array Nat) (cap : Nat) (bestDegree? : Option Nat)
    (shift : Array Nat) : Array Nat
```

`CompPoly.PolynomialMatrix.Approximant.AdaptiveSolveState` (structure, [line 455](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L455))

> State carried between adaptive solution-basis rounds.  `filtered`
> accumulates the exact solution rows found across all rounds.

```lean
structure AdaptiveSolveState (F : Type*) [Zero F] where
  profile : PivotDegreeProfile
  budgets : Array Nat
  filtered : PolynomialMatrix F
  raw : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.adaptiveSolutionRound` (definition, [line 464](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L464))

> One adaptive round: solve the chunked exact-nullspace problem for the
> current window assignment, keep the rows that satisfy the original diagonal
> congruences, and merge the observed shifted pivot degrees into the profile.

```lean
def adaptiveSolutionRound
    (mulCtx : CPolynomial.MulContext F) (modCtx : CPolynomial.ModContext F)
    (pmCtx : PMBasisContext F) (equation : ModularEquation F)
    (shift : Array Nat) (state : AdaptiveSolveState F) : AdaptiveSolveState F
```

`CompPoly.PolynomialMatrix.Approximant.adaptiveSolutionLoop` (definition, [line 484](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L484))

> Fuel-bounded adaptive window-escalation loop.  Rounds stop as soon as the
> caller's degree bound is already met by the best exact row found, or every
> principal coordinate is settled: discovered, saturated, or unable to beat the
> best solution row already in hand.

```lean
def adaptiveSolutionLoop
    (mulCtx : CPolynomial.MulContext F) (modCtx : CPolynomial.ModContext F)
    (pmCtx : PMBasisContext F) (equation : ModularEquation F)
    (shift : Array Nat) (degreeBound? : Option Nat) (cap : Nat) :
    Nat → AdaptiveSolveState F → AdaptiveSolveState F
```

`CompPoly.PolynomialMatrix.Approximant.adaptiveSolutionBasis` (definition, [line 522](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L522))

> Run the adaptive degree-first solver: discover the shifted pivot-degree
> profile with geometrically growing per-coordinate windows, where the final
> round doubles as the known-degree reconstruction for all discovered
> coordinates.  The initial window is one chunk per coordinate.  A caller with
> a degree bound stops the escalation as soon as the bound is met.

```lean
def adaptiveSolutionBasis
    (mulCtx : CPolynomial.MulContext F) (modCtx : CPolynomial.ModContext F)
    (pmCtx : PMBasisContext F) (equation : ModularEquation F)
    (shift : Array Nat) (degreeBound? : Option Nat) : AdaptiveSolveState F
```

`CompPoly.PolynomialMatrix.Approximant.discoverPivotDegreeProfileViaPMBasis` (definition, [line 536](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L536))

> Discover the shifted pivot-degree profile through the adaptive solver.

```lean
def discoverPivotDegreeProfileViaPMBasis
    (mulCtx : CPolynomial.MulContext F) (modCtx : CPolynomial.ModContext F)
    (pmCtx : PMBasisContext F) (equation : ModularEquation F)
    (shift : Array Nat) : PivotDegreeProfile
```

`CompPoly.PolynomialMatrix.Approximant.repairSolutionRowsViaPMBasis` (definition, [line 552](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L552))

> One residual reconstruction pass.  If compressed rows `B` are not themselves
> exact modular solutions, solve for polynomial combinations `C` such that
> `C * (B * F mod M) = 0 mod M`, then return `C * B`.  The residual equation is
> solved with the same adaptive solver, without a further repair recursion.
>
> The candidate rows are first reduced to one representative per shifted leading
> position.  The reduction steps are unimodular, so the generated row module is
> unchanged, while the residual equation's solution width stays bounded by the
> principal width instead of the raw candidate count; without this bound the
> repair solve can be quadratically wider than the original equation.

```lean
def repairSolutionRowsViaPMBasis
    (mulCtx : CPolynomial.MulContext F) (modCtx : CPolynomial.ModContext F)
    (pmCtx : PMBasisContext F) (equation : ModularEquation F)
    (shift : Array Nat) (rows : PolynomialMatrix F) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.debugUnchunkedFilteredSolutionBasisViaPMBasis` (definition, [line 569](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L569))

> Debug helper for tiny problems that intentionally disables
> principal-coordinate chunking, keeping an unchunked solve available for
> inspection without letting the production context bypass partial
> linearization.

```lean
def debugUnchunkedFilteredSolutionBasisViaPMBasis
    (mulCtx : CPolynomial.MulContext F) (modCtx : CPolynomial.ModContext F)
    (pmCtx : PMBasisContext F) (equation : ModularEquation F)
    (shift : Array Nat) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.knownDegreeFilteredSolutionBasisViaPMBasis` (definition, [line 580](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L580))

> Known-degree reconstruction followed by the original diagonal-equation
> guard.  The reconstruction plan is built from discovered shifted pivot degrees,
> solved as a chunked exact-nullspace PM-basis problem, and compressed back to the
> principal solution coordinates.

```lean
def knownDegreeFilteredSolutionBasisViaPMBasis
    (mulCtx : CPolynomial.MulContext F) (modCtx : CPolynomial.ModContext F)
    (pmCtx : PMBasisContext F) (equation : ModularEquation F)
    (shift : Array Nat) (profile : PivotDegreeProfile) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.filteredSolutionBasisViaPMBasis` (definition, [line 612](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L612))

> Solver exposed through the modular-equation context: run the adaptive
> degree-first window-escalation loop, whose final round is the known-degree
> reconstruction for every discovered coordinate, then back it with a certified
> verification solve.  When the caller supplies a degree bound and the best
> exact degree already found meets it, the adaptive candidate set is returned
> as-is: any solution within the bound is then matched by an adaptive row up to
> the bound, so the certified solve adds nothing the caller can observe.
> Otherwise a certified verification solve runs over the gated window —
> `min(bound, cap) + maxShift` with a bound, the best-degree-shrunk window
> without one — and the union of both filtered candidate sets is returned:
> solutions at or above the adaptive best are dominated by the adaptive rows;
> solutions strictly below it lie inside the certified window, whose orders rule
> out uncertified relaxed rows — so the union always contains an exact row of
> minimal shifted degree, including in the partial-masking regime where
> uncertified chunked-kernel rows crowd lower exact solutions out of every
> adaptive round.  The adaptive rows come first, so ties keep the adaptive
> choice.  The residual repair pass remains as a guard when both candidate sets
> are empty.  The filter, verification, and repair are semantic guards around
> the exact-nullspace bridge; they do not call any alternate interpolation
> backend.

```lean
def filteredSolutionBasisViaPMBasis
    (mulCtx : CPolynomial.MulContext F) (modCtx : CPolynomial.ModContext F)
    (pmCtx : PMBasisContext F) (equation : ModularEquation F)
    (shift : Array Nat) (degreeBound? : Option Nat) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.rowSatisfiesModularBool_of_mem_filterModularSolutionRows` (theorem, [line 632](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L632))

> Rows kept by the modular solution filter satisfy the modular predicate.

```lean
theorem rowSatisfiesModularBool_of_mem_filterModularSolutionRows
    {mulCtx : CPolynomial.MulContext F} {modCtx : CPolynomial.ModContext F}
    {equation : ModularEquation F} {rows : PolynomialMatrix F}
    {row : PolynomialRow F}
    (hrow : row ∈ MatrixRows (filterModularSolutionRows mulCtx modCtx equation rows)) :
    rowSatisfiesModularBool mulCtx modCtx row equation.matrix equation.moduli = true
```

`CompPoly.PolynomialMatrix.Approximant.adaptiveSolutionRound_filtered_sound` (theorem, [line 646](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L646))

> One adaptive round preserves modular soundness of the accumulated filtered
> rows.

```lean
theorem adaptiveSolutionRound_filtered_sound
    {mulCtx : CPolynomial.MulContext F} {modCtx : CPolynomial.ModContext F}
    {pmCtx : PMBasisContext F} {equation : ModularEquation F}
    {shift : Array Nat} {state : AdaptiveSolveState F}
    (hstate : ∀ row ∈ MatrixRows state.filtered,
      rowSatisfiesModularBool mulCtx modCtx row equation.matrix equation.moduli = true) :
    ∀ row ∈ MatrixRows
        (adaptiveSolutionRound mulCtx modCtx pmCtx equation shift state).filtered,
      rowSatisfiesModularBool mulCtx modCtx row equation.matrix equation.moduli = true
```

`CompPoly.PolynomialMatrix.Approximant.adaptiveSolutionLoop_filtered_sound` (theorem, [line 664](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L664))

> The adaptive escalation loop preserves modular soundness of the accumulated
> filtered rows.

```lean
theorem adaptiveSolutionLoop_filtered_sound
    {mulCtx : CPolynomial.MulContext F} {modCtx : CPolynomial.ModContext F}
    {pmCtx : PMBasisContext F} {equation : ModularEquation F}
    {shift : Array Nat} {degreeBound? : Option Nat} {cap : Nat} :
    ∀ (fuel : Nat) (state : AdaptiveSolveState F),
      (∀ row ∈ MatrixRows state.filtered,
        rowSatisfiesModularBool mulCtx modCtx row equation.matrix equation.moduli = true) →
      ∀ row ∈ MatrixRows
          (adaptiveSolutionLoop mulCtx modCtx pmCtx equation shift degreeBound? cap
            fuel state).filtered,
        rowSatisfiesModularBool mulCtx modCtx row equation.matrix equation.moduli = true
```

`CompPoly.PolynomialMatrix.Approximant.adaptiveSolutionBasis_filtered_sound` (theorem, [line 699](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L699))

> Rows accumulated by the adaptive solver satisfy the modular predicate.

```lean
theorem adaptiveSolutionBasis_filtered_sound
    {mulCtx : CPolynomial.MulContext F} {modCtx : CPolynomial.ModContext F}
    {pmCtx : PMBasisContext F} {equation : ModularEquation F}
    {shift : Array Nat} {degreeBound? : Option Nat} :
    ∀ row ∈ MatrixRows
        (adaptiveSolutionBasis mulCtx modCtx pmCtx equation shift
          degreeBound?).filtered,
      rowSatisfiesModularBool mulCtx modCtx row equation.matrix equation.moduli = true
```

`CompPoly.PolynomialMatrix.Approximant.filteredSolutionBasisViaPMBasis_sound` (theorem, [line 713](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L713))

> Every row returned by the filtered PM-basis modular solver satisfies the
> original diagonal modular equation.

```lean
theorem filteredSolutionBasisViaPMBasis_sound
    {mulCtx : CPolynomial.MulContext F} {modCtx : CPolynomial.ModContext F}
    {pmCtx : PMBasisContext F} {equation : ModularEquation F}
    {shift : Array Nat} {degreeBound? : Option Nat} {row : PolynomialRow F}
    (hrow : row ∈ MatrixRows
      (filteredSolutionBasisViaPMBasis mulCtx modCtx pmCtx equation shift
        degreeBound?)) :
    rowSatisfiesModularBool mulCtx modCtx row equation.matrix equation.moduli = true
```

`CompPoly.PolynomialMatrix.Approximant.ModularSolutionBasisContext` (structure, [line 742](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean#L742))

> Modular-equation solution-basis context with theorem fields.
>
> The solver takes an optional caller-supplied degree bound.  The
> completeness/minimality contract is bound-relative: for any nonzero in-width
> solution row of the diagonal modular equation whose shifted degree fits the
> bound (vacuous for `none`), the returned basis stays inside the principal
> width and contains a row whose shifted degree does not exceed the bound — the
> given solution's own degree when no bound is supplied.  The contract assumes
> monic moduli, a relation matrix wide enough to expose every modular column to
> the executable row predicate, and a shift aligned with the principal solution
> width.

```lean
structure ModularSolutionBasisContext (F : Type*) [Field F] [BEq F] [LawfulBEq F] where
  mulContext : CPolynomial.MulContext F
  modContext : CPolynomial.ModContext F
  solutionBasis : ModularEquation F → Array Nat → Option Nat → PolynomialMatrix F
  sound :
    ∀ equation shift degreeBound? row,
      row ∈ MatrixRows (solutionBasis equation shift degreeBound?) →
        rowSatisfiesModularBool mulContext modContext row equation.matrix equation.moduli = true
  complete_minimal :
    ∀ equation shift degreeBound? row rowDegree,
      (∀ b, b < equation.moduli.size → (equation.moduli.getD b 0).monic) →
      equation.moduli.size ≤ MatrixWidth equation.matrix →
      shift.size = equation.solutionWidth →
      rowSatisfiesModularBool mulContext modContext row equation.matrix
          equation.moduli = true →
      rowIsZero row = false →
      row.size ≤ equation.solutionWidth →
      rowShiftedDegree? row shift = some rowDegree →
      (∀ bound, degreeBound? = some bound → rowDegree ≤ bound) →
        (∀ basisRow,
          basisRow ∈ MatrixRows (solutionBasis equation shift degreeBound?) →
            basisRow.size ≤ equation.solutionWidth) ∧
        ∃ basisRow degree,
          basisRow ∈ MatrixRows (solutionBasis equation shift degreeBound?) ∧
          rowShiftedDegree? basisRow shift = some degree ∧
          degree ≤ degreeBound?.getD rowDegree
```

## Depends on

- [Recursive PM-Basis Driver](../pmbasis-2/recursion.md)
- [Partial-Linearization Parameters](../partiallinearization.md)

## Proof depends on

- [Row Span for Polynomial Matrices](../../rowspan.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation/Basic.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.ModularEquation.Basic.json)
