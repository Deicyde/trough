---
catalog: module
lean: Cslib.Logic.InferenceSystem, Cslib.Logic.InferenceSystem.Default, Cslib.Logic.HasInferenceSystem, Cslib.Logic.InferenceSystem.rwConclusion, Cslib.Logic.InferenceSystem.DerivableIn, Cslib.Logic.InferenceSystem.Derivable, Cslib.Logic.InferenceSystem.DerivableIn.fromDerivation, Cslib.Logic.InferenceSystem.DerivableIn.toDerivation, Cslib.Logic.InferenceSystem.delabInferenceSystem
statement: formalized
proof: formalized
---

# Inference systems

`Cslib.Foundations.Logic.InferenceSystem.Defs`, in [Cslib/Foundations/Logic/InferenceSystem/Defs.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/InferenceSystem/Defs.lean), by Fabrizio Montesi.

> This module defines the basic classes and notation for *inference systems* -- systems for deriving
> conclusions from premises.
>
> We intend inference systems broadly, as in theory of programming languages. In applications to
> logic, for example, we use inference systems to capture both the concepts of satisfiability and
> proof systems.

`Cslib.Logic.InferenceSystem` (class, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/InferenceSystem/Defs.lean#L30))

> The notation typeclass for inference systems.
> This enables the notation `S⇓a`, where `S` is a tag for the inference system and `a : α`
> is a derivable value.

```lean
class InferenceSystem (S : Type*) (α : Type*) where
  /--
  `S⇓a` is a derivation of `a`, that is, a witness that `a` is derivable in the system `S`.
  The meaning of this notation is type-dependent.
  -/
  derivation (a : α) : Sort v
```

`Cslib.Logic.InferenceSystem.Default` (opaque constant, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/InferenceSystem/Defs.lean#L38))

> Default tag for inference system instances. `⇓a` is short for `Default⇓a`.

```lean
opaque InferenceSystem.Default : Type
```

`Cslib.Logic.HasInferenceSystem` (abbreviation, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/InferenceSystem/Defs.lean#L41))

> Class for types (`α`) that have a canonical inference system.

```lean
abbrev HasInferenceSystem
```

`Cslib.Logic.InferenceSystem.rwConclusion` (definition, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/InferenceSystem/Defs.lean#L49))

> Rewrites the conclusion of a proof into an equal one.

```lean
def rwConclusion [InferenceSystem S α] {Γ Δ : α} (h : Γ = Δ) (p : S⇓Γ) : S⇓Δ
```

`Cslib.Logic.InferenceSystem.DerivableIn` (definition, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/InferenceSystem/Defs.lean#L53))

> `a` is derivable in `S` if it is the conclusion of some derivation.

```lean
def DerivableIn S [InferenceSystem S α] (a : α)
```

`Cslib.Logic.InferenceSystem.Derivable` (abbreviation, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/InferenceSystem/Defs.lean#L56))

> `a : α` is derivable in the default inference system for `α`.

```lean
abbrev Derivable [InferenceSystem Default α]
```

`Cslib.Logic.InferenceSystem.DerivableIn.fromDerivation` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/InferenceSystem/Defs.lean#L59))

> Shows derivability from a derivation.

```lean
theorem DerivableIn.fromDerivation [InferenceSystem S α] {a : α} (d : S⇓a) : DerivableIn S a
```

`Cslib.Logic.InferenceSystem.DerivableIn.toDerivation` (definition, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/InferenceSystem/Defs.lean#L65))

> Extracts (noncomputably) a derivation from the fact that a conclusion is derivable.

```lean
noncomputable def DerivableIn.toDerivation [InferenceSystem S α] {a : α} (d : DerivableIn S a) :
    S⇓a
```

`Cslib.Logic.InferenceSystem.delabInferenceSystem` (definition, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/InferenceSystem/Defs.lean#L77))

> Delaborator that hides `InferenceSystem.Default` in uses of the `⇓a` notation.

```lean
meta def delabInferenceSystem : Delab
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Logic/InferenceSystem/Defs.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/InferenceSystem/Defs.lean)
