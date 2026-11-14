---
declaration: section
origin: cited
lean: OAI.PermanentBorder.permanent_cubic_lower_bounds, OAI.PermanentBorder.smooth_initial_form_lower_bound
statement: formalized
proof: formalized
---

# 108. A cubic permanent–determinant lower bound

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves an $\Omega(n^3)$ lower bound for the border determinantal complexity of the $n\times n$ permanent over ℂ. Even coefficientwise limits of determinants of affine-linear matrices require matrix size at least $cn^3$, for an absolute *c* > 0 and all sufficiently large *n*; the same bound therefore holds for exact representations.

## A cubic lower bound for border determinantal complexity of the permanent

We prove that the complex border determinantal complexity of the $m\times m$ permanent is $\Omega(m^3)$, allowing arbitrary affine-linear determinant representations and coefficientwise limits. It also gives cubic lower bounds for exact determinantal complexity and for the numbers of vertices and edges in affine-linear algebraic branching programs, including coefficientwise limits with a fixed vertex or edge budget.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves a cubic lower bound for both exact and border determinantal representations of the complex $m\times m$ permanent. For $m\ge1408$, every affine-linear determinant representation of size $n$, including coefficientwise limits, satisfies $n\ge m^3/(5529600e)$.

A general supporting theorem applies to a polynomial in $d\ge2$ variables whose first nonzero homogeneous Taylor term has degree $r\ge2$ and no nonzero singular zero. Its exact and border determinantal sizes are at least $(r-1)(d-1)/(4e)$. The paper's algebraic-branching-program consequences are outside these statements.

## Lean: Cubic lower bounds for permanent determinantal complexity

```lean
theorem permanent_cubic_lower_bounds :
    (∀ (m n : ℕ), 1408 ≤ m → HasBorderDeterminant n (permanentPolynomial m) →
      (m : ℝ)^3 / (5529600 * Real.exp 1) ≤ (n : ℝ)) ∧
    (∀ (m n : ℕ), 1408 ≤ m → HasExactDeterminant n (permanentPolynomial m) →
      (m : ℝ)^3 / (5529600 * Real.exp 1) ≤ (n : ℝ))
```

Stated in [PermanentCubic.lean, line 33](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PermanentCubic.lean#L33). Proved in [lean/OAI/Algebra/Determinantal/Main.lean, line 384](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Algebra/Determinantal/Main.lean#L384).

## Lean: Determinantal lower bound from a smooth initial form

```lean
theorem smooth_initial_form_lower_bound (d r : ℕ) (g : Poly (Fin d))
    (a : Fin d → ℂ) (hd : 2 ≤ d) (hr : 2 ≤ r)
    (hG : homogeneousComponent r
      (affineSubstitution a (fun i j : Fin d => if i = j then 1 else 0) g) ≠ 0)
    (hlow : ∀ j < r, homogeneousComponent j
      (affineSubstitution a (fun i j : Fin d => if i = j then 1 else 0) g) = 0)
    (hs : ∀ y : Fin d → ℂ,
      eval y (homogeneousComponent r
        (affineSubstitution a (fun i j : Fin d => if i = j then 1 else 0) g)) = 0 →
      (∀ i, eval y (pderiv i (homogeneousComponent r
        (affineSubstitution a (fun i j : Fin d => if i = j then 1 else 0) g))) = 0) →
      y = 0) :
    ∀ n : ℕ,
      (HasBorderDeterminant n g →
        ((r - 1 : ℕ) : ℝ) * ((d - 1 : ℕ) : ℝ) / (4 * Real.exp 1) ≤ (n : ℝ)) ∧
      (HasExactDeterminant n g →
        ((r - 1 : ℕ) : ℝ) * ((d - 1 : ℕ) : ℝ) / (4 * Real.exp 1) ≤ (n : ℝ))
```

Stated in [SmoothInitialForm.lean, line 35](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SmoothInitialForm.lean#L35). Proved in [lean/OAI/Algebra/Determinantal/InitialForm.lean, line 128](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Algebra/Determinantal/InitialForm.lean#L128).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/108.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/108.md)
