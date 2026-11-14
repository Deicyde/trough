---
catalog: module
lean: Cslib.Crypto.PRG.Generator, Cslib.Crypto.PRG.Adversary, Cslib.Crypto.PRG.Generator.coe_mk, Cslib.Crypto.PRG.Generator.IsExpanding, Cslib.Crypto.PRG.Generator.outputDist, Cslib.Crypto.PRG.Generator.realExperiment, Cslib.Crypto.PRG.Generator.idealExperiment, Cslib.Crypto.PRG.Generator.advantage, Cslib.Crypto.PRG.Generator.Secure
statement: formalized
proof: formalized
---

# Pseudorandom generators: games and concrete security

`Cslib.Crypto.Primitives.PRG.Defs`, in [Cslib/Crypto/Primitives/PRG/Defs.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Defs.lean), by Samuel Schlesinger.

> Attack Game 3.1 of [BonehShoup2023] compares a deterministic generator applied to a
> uniform seed with a uniform output. Adversaries are randomized Boolean tests. Security
> is relative to a caller-supplied predicate `Admissible`, with an explicit advantage bound.
> No computational model or efficiency assumption is built into the generator or the tests.
>
> `Generator.IsExpanding` records the cardinality condition separately from security.
> In particular, a generator need not expand, and an expanding generator need not be secure.
>
> ## References
>
> * [D. Boneh, V. Shoup, *A Graduate Course in Applied Cryptography*,
>   Version 0.6][BonehShoup2023], Section 3.1.

`Cslib.Crypto.PRG.Generator` (structure, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Defs.lean#L38))

> A deterministic generator with seed space `Seed` and output space `Output`.
> Efficiency, expansion, and security are separate properties.

```lean
structure Generator (Seed Output : Type*) where
  /-- Generate an output from a seed. -/
  toFun : Seed → Output
```

`Cslib.Crypto.PRG.Adversary` (abbreviation, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Defs.lean#L43))

> A randomized statistical test on the output space.

```lean
abbrev Adversary (Output : Type*)
```

`Cslib.Crypto.PRG.Generator.coe_mk` (theorem, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Defs.lean#L54))

```lean
theorem coe_mk (f : Seed → Output) : ⇑(Generator.mk f) = f
```

`Cslib.Crypto.PRG.Generator.IsExpanding` (definition, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Defs.lean#L57))

> A generator expands when its output space is strictly larger than its seed space.

```lean
def IsExpanding [Fintype Seed] [Fintype Output] (_G : Generator Seed Output) : Prop
```

`Cslib.Crypto.PRG.Generator.outputDist` (definition, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Defs.lean#L63))

> The distribution obtained by applying the generator to a uniform seed.

```lean
noncomputable def outputDist (G : Generator Seed Output) : PMF Output
```

`Cslib.Crypto.PRG.Generator.realExperiment` (definition, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Defs.lean#L67))

> Experiment 0 of Attack Game 3.1: give the adversary a generated output.

```lean
noncomputable def realExperiment (G : Generator Seed Output)
    (adversary : Adversary Output) : PMF Bool
```

`Cslib.Crypto.PRG.Generator.idealExperiment` (definition, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Defs.lean#L72))

> Experiment 1 of Attack Game 3.1: give the adversary a uniform output.

```lean
noncomputable def idealExperiment (adversary : Adversary Output) : PMF Bool
```

`Cslib.Crypto.PRG.Generator.advantage` (definition, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Defs.lean#L77))

> The absolute difference of the probabilities of outputting `true` in the two
> experiments, as in Attack Game 3.1 of [BonehShoup2023].

```lean
noncomputable def advantage (G : Generator Seed Output) (adversary : Adversary Output) : ℝ
```

`Cslib.Crypto.PRG.Generator.Secure` (definition, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Defs.lean#L83))

> Concrete security against admissible adversaries. The predicate is supplied by the
> caller, for example to restrict tests to a chosen computational resource bound.
> Taking `Admissible := fun _ => True` allows arbitrary adversaries.

```lean
def Secure (G : Generator Seed Output) (Admissible : Adversary Output → Prop)
    (ε : ℝ≥0) : Prop
```

## Depends on

- [PMF Utilities](../../../probability/pmf.md)

## Sources

- [Cslib/Crypto/Primitives/PRG/Defs.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Defs.lean)
