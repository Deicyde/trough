---
catalog: module
lean: Cslib.Crypto.PRG.Generator.advantage_nonneg, Cslib.Crypto.PRG.Generator.advantage_le_one, Cslib.Crypto.PRG.Generator.secure_one, Cslib.Crypto.PRG.Generator.advantage_const, Cslib.Crypto.PRG.Generator.secure_zero_of_outputDist_eq, Cslib.Crypto.PRG.Generator.secure_zero_iff_outputDist_eq_uniform, Cslib.Crypto.PRG.Generator.Secure.mono, Cslib.Crypto.PRG.Generator.Secure.of_admissible, Cslib.Crypto.PRG.Generator.rangeTest, Cslib.Crypto.PRG.Generator.rangeAdversary, Cslib.Crypto.PRG.Generator.realExperiment_rangeAdversary, Cslib.Crypto.PRG.Generator.idealExperiment_rangeAdversary, Cslib.Crypto.PRG.Generator.advantage_rangeAdversary, Cslib.Crypto.PRG.Generator.one_sub_card_div_le_advantage_rangeAdversary, Cslib.Crypto.PRG.Generator.not_secure_of_rangeAdversary, Cslib.Crypto.PRG.Generator.not_secure_zero_of_isExpanding, Cslib.Crypto.PRG.Generator.not_exists_isExpanding_secure_zero, Cslib.Crypto.PRG.Generator.prod, Cslib.Crypto.PRG.Generator.outputDist_prod, Cslib.Crypto.PRG.Generator.leftReduction, Cslib.Crypto.PRG.Generator.rightReduction, Cslib.Crypto.PRG.Generator.realExperiment_prod, Cslib.Crypto.PRG.Generator.idealExperiment_leftReduction, Cslib.Crypto.PRG.Generator.idealExperiment_rightReduction, Cslib.Crypto.PRG.Generator.advantage_prod_le, Cslib.Crypto.PRG.Generator.Secure.prod
statement: formalized
proof: formalized
---

# Pseudorandom generators against arbitrary adversaries

`Cslib.Crypto.Primitives.PRG.Basic`, in [Cslib/Crypto/Primitives/PRG/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean), by Samuel Schlesinger.

> The range-membership test accepts every generated output, whereas it accepts a uniform
> output with probability `|range G| / |Output|`. Its advantage is therefore at least
> `1 - |Seed| / |Output|`. This proves that an expanding generator cannot have zero
> advantage against arbitrary adversaries, and gives a quantitative obstruction for
> every smaller error bound. No injectivity assumption on the generator is needed.

`Cslib.Crypto.PRG.Generator.advantage_nonneg` (theorem, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L34))

> Advantage is nonnegative.

```lean
theorem advantage_nonneg (G : Generator Seed Output) (adversary : Adversary Output) :
    0 ≤ G.advantage adversary
```

`Cslib.Crypto.PRG.Generator.advantage_le_one` (theorem, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L38))

> Advantage is at most one, with the normalization of Attack Game 3.1.

```lean
theorem advantage_le_one (G : Generator Seed Output) (adversary : Adversary Output) :
    G.advantage adversary ≤ 1
```

`Cslib.Crypto.PRG.Generator.secure_one` (theorem, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L51))

> Error one imposes no restriction on a generator.

```lean
theorem secure_one (G : Generator Seed Output) (Admissible : Adversary Output → Prop) :
    G.Secure Admissible 1
```

`Cslib.Crypto.PRG.Generator.advantage_const` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L56))

> A test whose output distribution is independent of its input has zero advantage.

```lean
theorem advantage_const (G : Generator Seed Output) (p : PMF Bool) :
    G.advantage (fun _ => p) = 0
```

`Cslib.Crypto.PRG.Generator.secure_zero_of_outputDist_eq` (theorem, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L61))

> A generator with exactly uniform output is secure with zero error against any tests.

```lean
theorem secure_zero_of_outputDist_eq (G : Generator Seed Output)
    (hG : G.outputDist = uniformOfFintype Output)
    (Admissible : Adversary Output → Prop) : G.Secure Admissible 0
```

`Cslib.Crypto.PRG.Generator.secure_zero_iff_outputDist_eq_uniform` (theorem, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L68))

> Zero-error security against arbitrary tests is equivalent to exactly uniform output.

```lean
theorem secure_zero_iff_outputDist_eq_uniform (G : Generator Seed Output) :
    G.Secure (fun _ => True) 0 ↔ G.outputDist = uniformOfFintype Output
```

`Cslib.Crypto.PRG.Generator.Secure.mono` (theorem, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L78))

> Enlarging the allowed advantage preserves security.

```lean
theorem Secure.mono {G : Generator Seed Output} {Admissible : Adversary Output → Prop} :
    Monotone (G.Secure Admissible)
```

`Cslib.Crypto.PRG.Generator.Secure.of_admissible` (theorem, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L83))

> Security against a larger class of adversaries implies security against a smaller class.

```lean
theorem Secure.of_admissible {G : Generator Seed Output}
    {Admissible Restricted : Adversary Output → Prop} {ε : ℝ≥0}
    (h : G.Secure Admissible ε) (hsub : ∀ adversary, Restricted adversary → Admissible adversary) :
    G.Secure Restricted ε
```

`Cslib.Crypto.PRG.Generator.rangeTest` (definition, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L94))

> Decide range membership by finite seed enumeration and output comparison.

```lean
def rangeTest (G : Generator Seed Output) (output : Output) : Bool
```

`Cslib.Crypto.PRG.Generator.rangeAdversary` (definition, [line 99](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L99))

> The deterministic adversary that tests membership in the generator's range.

```lean
noncomputable def rangeAdversary (G : Generator Seed Output) : Adversary Output
```

`Cslib.Crypto.PRG.Generator.realExperiment_rangeAdversary` (theorem, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L105))

> The range test always accepts a generated output.

```lean
theorem realExperiment_rangeAdversary (G : Generator Seed Output) :
    G.realExperiment G.rangeAdversary = PMF.pure true
```

`Cslib.Crypto.PRG.Generator.idealExperiment_rangeAdversary` (theorem, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L113))

> The range test's acceptance probability under uniform sampling is the fraction
> of outputs in the range.

```lean
theorem idealExperiment_rangeAdversary (G : Generator Seed Output) :
    (idealExperiment G.rangeAdversary true).toReal =
      Nat.card (Set.range G) / (Fintype.card Output : ℝ)
```

`Cslib.Crypto.PRG.Generator.advantage_rangeAdversary` (theorem, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L123))

> The exact advantage of the range-membership adversary.

```lean
theorem advantage_rangeAdversary (G : Generator Seed Output) :
    G.advantage G.rangeAdversary =
      1 - Nat.card (Set.range G) / (Fintype.card Output : ℝ)
```

`Cslib.Crypto.PRG.Generator.one_sub_card_div_le_advantage_rangeAdversary` (theorem, [line 135](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L135))

> Every generator has an unbounded distinguisher with advantage at least
> `1 - |Seed| / |Output|`. Collisions can only improve this attack.

```lean
theorem one_sub_card_div_le_advantage_rangeAdversary (G : Generator Seed Output) :
    1 - Fintype.card Seed / (Fintype.card Output : ℝ) ≤
      G.advantage G.rangeAdversary
```

`Cslib.Crypto.PRG.Generator.not_secure_of_rangeAdversary` (theorem, [line 144](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L144))

> Security is impossible below the range-test bound whenever that test is admissible.

```lean
theorem not_secure_of_rangeAdversary (G : Generator Seed Output)
    {Admissible : Adversary Output → Prop} {ε : ℝ≥0}
    (ha : Admissible G.rangeAdversary)
    (hε : (ε : ℝ) < 1 - Fintype.card Seed / (Fintype.card Output : ℝ)) :
    ¬ G.Secure Admissible ε
```

`Cslib.Crypto.PRG.Generator.not_secure_zero_of_isExpanding` (theorem, [line 155](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L155))

> An expanding generator cannot be perfectly secure against arbitrary adversaries.

```lean
theorem not_secure_zero_of_isExpanding (G : Generator Seed Output) (hG : G.IsExpanding) :
    ¬ G.Secure (fun _ => True) 0
```

`Cslib.Crypto.PRG.Generator.not_exists_isExpanding_secure_zero` (theorem, [line 164](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L164))

> There is no expanding, perfectly secure generator against arbitrary adversaries.

```lean
theorem not_exists_isExpanding_secure_zero :
    ¬ ∃ G : Generator Seed Output, G.IsExpanding ∧ G.Secure (fun _ => True) 0
```

`Cslib.Crypto.PRG.Generator.prod` (definition, [line 173](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L173))

> Apply `G` separately to each component of a pair of seeds.

```lean
def prod (G : Generator Seed Output) : Generator (Seed × Seed) (Output × Output)
```

`Cslib.Crypto.PRG.Generator.outputDist_prod` (theorem, [line 178](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L178))

> The output distribution of `G.prod` is two independent draws from `G.outputDist`.

```lean
theorem outputDist_prod (G : Generator Seed Output) :
    G.prod.outputDist =
      G.outputDist.bind fun y₁ => G.outputDist.map fun y₂ => (y₁, y₂)
```

`Cslib.Crypto.PRG.Generator.leftReduction` (definition, [line 187](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L187))

> First hybrid distinguisher: given `y₁`, sample `y₂ ← G.outputDist` and run `A (y₁, y₂)`.

```lean
noncomputable def leftReduction (G : Generator Seed Output)
    (A : Adversary (Output × Output)) : Adversary Output
```

`Cslib.Crypto.PRG.Generator.rightReduction` (definition, [line 192](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L192))

> Second hybrid distinguisher: given `y₂`, sample `u₁ ←$ Output` and run `A (u₁, y₂)`.

```lean
noncomputable def rightReduction
    (A : Adversary (Output × Output)) : Adversary Output
```

`Cslib.Crypto.PRG.Generator.realExperiment_prod` (theorem, [line 199](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L199))

> Real experiment for `G.prod` equals the real experiment for `G` against
> `leftReduction`.

```lean
theorem realExperiment_prod (G : Generator Seed Output)
    (A : Adversary (Output × Output)) :
    G.prod.realExperiment A = G.realExperiment (G.leftReduction A)
```

`Cslib.Crypto.PRG.Generator.idealExperiment_leftReduction` (theorem, [line 210](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L210))

> Ideal experiment against `leftReduction` equals the real experiment against
> `rightReduction` (both equal the hybrid distribution `(u₁, G(x₂))`).

```lean
theorem idealExperiment_leftReduction (G : Generator Seed Output)
    (A : Adversary (Output × Output)) :
    idealExperiment (G.leftReduction A) = G.realExperiment (rightReduction A)
```

`Cslib.Crypto.PRG.Generator.idealExperiment_rightReduction` (theorem, [line 217](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L217))

> Ideal experiment against `rightReduction` equals the ideal experiment for `G.prod`.

```lean
theorem idealExperiment_rightReduction (A : Adversary (Output × Output)) :
    idealExperiment (rightReduction A) = idealExperiment A
```

`Cslib.Crypto.PRG.Generator.advantage_prod_le` (theorem, [line 225](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L225))

> Hybrid advantage bound: `Adv(G.prod, A) ≤ Adv(G, leftReduction) + Adv(G, rightReduction)`.

```lean
theorem advantage_prod_le (G : Generator Seed Output)
    (A : Adversary (Output × Output)) :
    G.prod.advantage A ≤
      G.advantage (G.leftReduction A) + G.advantage (rightReduction A)
```

`Cslib.Crypto.PRG.Generator.Secure.prod` (theorem, [line 236](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean#L236))

> Concrete security of `H(x₁, x₂) = (G(x₁), G(x₂))` via a two-step hybrid argument.

```lean
theorem Secure.prod {G : Generator Seed Output}
    {Admissible₁ : Adversary Output → Prop}
    {Admissible₂ : Adversary (Output × Output) → Prop}
    {ε : ℝ≥0}
    (hG : G.Secure Admissible₁ ε)
    (hLeft : ∀ A, Admissible₂ A → Admissible₁ (G.leftReduction A))
    (hRight : ∀ A, Admissible₂ A → Admissible₁ (rightReduction A)) :
    G.prod.Secure Admissible₂ (2 * ε)
```

## Depends on

- [Pseudorandom generators: games and concrete security](defs.md)

## Sources

- [Cslib/Crypto/Primitives/PRG/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Primitives/PRG/Basic.lean)
