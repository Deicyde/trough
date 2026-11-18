---
declaration: module
origin: cited
lean: TestFunction.precompTranslationSupportedCLM, TestFunction.precompTranslationCLM, TestFunction.precompTranslationCLM_apply
statement: formalized
proof: formalized
---

# Translation of test functions

The module `PhyslibAlpha.Mathematics.Distribution.Translation`, [PhyslibAlpha/Mathematics/Distribution/Translation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/Translation.lean): 3 declarations, 3 with a docstring.

> Translation is continuous on the space of test functions.

## i. Overview

> Composition with a translation `x ↦ x + b` maps a smooth function with support in a compact set
> `K` to a smooth function with support in the translated set. It does not change the norms of the
> derivatives. So it is continuous between the spaces of test functions with fixed support. It is
> then continuous on all test functions.

## ii. Key results

> - `TestFunction.precompTranslationSupportedCLM` : the pullback between fixed-support spaces.
> - `TestFunction.precompTranslationCLM` : the pullback is continuous on test functions.

## iv. References

> None.

## A. The pullback along a translation

> - `TestFunction.precompTranslationSupportedCLM` : the pullback between fixed-support spaces.
> - `TestFunction.precompTranslationCLM` : the pullback is continuous on test functions.

**`TestFunction.precompTranslationSupportedCLM`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/Translation.lean#L55).

> The pullback along a translation between fixed-support smooth test spaces.

```lean
def precompTranslationSupportedCLM (b : A) (K : Compacts A) :
    ContDiffMapSupportedIn A F ⊤ K →L[ℝ]
      ContDiffMapSupportedIn A F ⊤ (K.map (fun x => x - b) (continuous_id.sub continuous_const))
```

**`TestFunction.precompTranslationCLM`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/Translation.lean#L84).

> The pullback along a translation is continuous on test functions.

```lean
def precompTranslationCLM (b : A) : 𝓓((⊤ : Opens A), F) →L[ℝ] 𝓓((⊤ : Opens A), F)
```

**`TestFunction.precompTranslationCLM_apply`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/Translation.lean#L97).

> The pullback along a translation evaluates the function at the translated point.

```lean
lemma precompTranslationCLM_apply (b : A) (f : 𝓓((⊤ : Opens A), F)) (x : A) :
    precompTranslationCLM b f x = f (x + b)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Distribution/Translation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/Translation.lean)
