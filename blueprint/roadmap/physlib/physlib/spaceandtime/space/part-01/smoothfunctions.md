---
declaration: module
origin: cited
lean: Space.cmap, Space.cmap_apply
statement: formalized
proof: formalized
---

# Smooth real-valued functions on space

The module `Physlib.SpaceAndTime.Space.SmoothFunctions`, [Physlib/SpaceAndTime/Space/SmoothFunctions.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/SmoothFunctions.lean): 2 declarations, 1 with a docstring.

> `Space.cmap` bundles a smooth real-valued function on `Space d`, given as a plain function
> together with a `ContDiff` proof, into the space of bundled smooth maps
> `C^⊤⟮𝓘(ℝ, Space d), Space d; 𝓘(ℝ, ℝ), ℝ⟯`. Such bundled maps are, for instance, the test
> functions on which the mass distribution of a rigid body acts.

**`Space.cmap`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/SmoothFunctions.lean#L29).

> Bundle a smooth real-valued function on `Space d` as an element of the space of bundled
> smooth maps. Keeping this as a named constructor ensures the resulting type head stays
> `ContMDiffMap`, so the module/ring operations and `comp` resolve correctly.

```lean
def cmap {d : ℕ} (f : Space d → ℝ) (hf : ContDiff ℝ ⊤ f) :
    C^⊤⟮𝓘(ℝ, Space d), Space d; 𝓘(ℝ, ℝ), ℝ⟯
```

**`Space.cmap_apply`**, a lemma, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/SmoothFunctions.lean#L33).

```lean
lemma cmap_apply {d : ℕ} (f : Space d → ℝ) (hf : ContDiff ℝ ⊤ f) (y : Space d) :
    cmap f hf y = f y
```

## Depends on

- [The structure of a module on Space](module.md)

## Sources

- [Physlib/SpaceAndTime/Space/SmoothFunctions.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/SmoothFunctions.lean)
