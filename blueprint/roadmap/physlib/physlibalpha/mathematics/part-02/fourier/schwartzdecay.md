---
declaration: module
origin: cited
lean: SchwartzMap.exists_integral_norm_fourier_le
statement: formalized
proof: formalized
---

# The integral of a Fourier transform is bounded by Schwartz seminorms

The module `PhyslibAlpha.Mathematics.Fourier.SchwartzDecay`, [PhyslibAlpha/Mathematics/Fourier/SchwartzDecay.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/SchwartzDecay.lean): 1 declaration, 1 with a docstring.

> The `L¹` norm of the Fourier transform of a Schwartz function is bounded by finitely many
> Schwartz seminorms of the function.

## i. Overview

> The Fourier transform is continuous on Schwartz space. A weighted supremum of the transform is
> therefore bounded by finitely many seminorms of the function. The weight `(1 + ‖ξ‖)^n` with
> `n` above the dimension makes the transform integrable. The constants do not depend on the
> function.

## ii. Key results

> - `exists_integral_norm_fourier_le` : the bound of `∫ ‖𝓕 g‖` by seminorms of `g`.

## iv. References

> None.

## A. The bound

> - `exists_integral_norm_fourier_le` : the bound of `∫ ‖𝓕 g‖` by seminorms of `g`.

**`SchwartzMap.exists_integral_norm_fourier_le`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/SchwartzDecay.lean#L56).

> **The `L¹` norm of a Fourier transform.** The integral of `‖𝓕 g‖` is bounded by a constant
> times a finite supremum of Schwartz seminorms of `g`.

```lean
lemma exists_integral_norm_fourier_le :
    ∃ (S : Finset (ℕ × ℕ)) (C : ℝ), 0 ≤ C ∧ ∀ g : 𝓢(E, F),
      ∫ ξ : E, ‖𝓕 g ξ‖ ≤ C * (S.sup (schwartzSeminormFamily ℂ E F)) g
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [Pointwise polynomial decay of Schwartz functions](../distribution/schwartzpointwise.md)

## Sources

- [PhyslibAlpha/Mathematics/Fourier/SchwartzDecay.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/SchwartzDecay.lean)
