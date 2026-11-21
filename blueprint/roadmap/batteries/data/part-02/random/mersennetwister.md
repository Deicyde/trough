---
catalog: module
lean: Batteries.Random.MersenneTwister.Config, Batteries.Random.MersenneTwister.Config.zero_lt_wordSize, Batteries.Random.MersenneTwister.Config.zero_lt_stateSize, Batteries.Random.MersenneTwister.State, Batteries.Random.MersenneTwister.Config.init, Batteries.Random.MersenneTwister.State.twist, Batteries.Random.MersenneTwister.State.update, Batteries.Random.MersenneTwister.State.next, Batteries.Random.MersenneTwister.mt19937, Batteries.Random.MersenneTwister.mt19937_64
statement: formalized
proof: formalized
---

# Mersenne Twister

`Batteries.Data.Random.MersenneTwister`, in [Batteries/Data/Random/MersenneTwister.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Random/MersenneTwister.lean), by François G. Dorais.

> Generic implementation for the Mersenne Twister pseudorandom number generator.
>
> All choices of parameters from Matsumoto and Nishimura (1998) are supported, along with later
> refinements. Parameters for the standard 32-bit MT19937 and 64-bit MT19937-64 algorithms are
> provided. Both `RandomGen` and `Stream` interfaces are provided.
>
> Use `mt19937.init seed` to create a MT19937 PRNG with a 32 bit seed value; use
> `mt19937_64.init seed` to create a MT19937-64 PRNG with a 64 bit seed value. If omitted, default
> seed choices will be used.
>
> Sample usage:
> ```
> import Batteries.Data.Random.MersenneTwister
>
> open Batteries.Random.MersenneTwister
>
> def mtgen := mt19937.init -- default seed 4357
>
> #eval (Stream.take mtgen 5).fst -- [874448474, 2424656266, 2174085406, 1265871120, 3155244894]
> ```
>
> ### References:
>
> - Matsumoto, Makoto and Nishimura, Takuji (1998),
>   [**Mersenne twister: A 623-dimensionally equidistributed uniform pseudo-random number generator**](https://doi.org/10.1145/272991.272995),
>   ACM Trans. Model. Comput. Simul. 8, No. 1, 3-30.
>   [ZBL0917.65005](https://zbmath.org/?q=an:0917.65005).
>
> - Nishimura, Takuji (2000),
>   [**Tables of 64-bit Mersenne twisters**](https://doi.org/10.1145/369534.369540),
>   ACM Trans. Model. Comput. Simul. 10, No. 4, 348-357.
>   [ZBL1390.65014](https://zbmath.org/?q=an:1390.65014).

`Batteries.Random.MersenneTwister.Config` (structure, [line 54](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Random/MersenneTwister.lean#L54))

> Mersenne Twister configuration.
>
> Letters in parentheses correspond to variable names used by Matsumoto and Nishimura (1998) and
> Nishimura (2000).

```lean
structure Config where
  /-- Word size (`w`). -/
  wordSize : Nat
  /-- Degree of recurrence (`n`). -/
  stateSize : Nat
  /-- Middle word (`m`). -/
  shiftSize : Fin stateSize
  /-- Twist value (`r`). -/
  maskBits : Fin wordSize
  /-- Coefficients of the twist matrix (`a`). -/
  xorMask : BitVec wordSize
  /-- Tempering shift parameters (`u`, `s`, `t`, `l`). -/
  temperingShifts : Nat × Nat × Nat × Nat
  /-- Tempering mask parameters (`d`, `b`, `c`). -/
  temperingMasks : BitVec wordSize × BitVec wordSize × BitVec wordSize
  /-- Initialization multiplier (`f`). -/
  initMult : BitVec wordSize
  /-- Default initialization seed value. -/
  initSeed : BitVec wordSize
```

`Batteries.Random.MersenneTwister.Config.zero_lt_wordSize` (theorem, [line 80](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Random/MersenneTwister.lean#L80))

```lean
theorem Config.zero_lt_wordSize (cfg : Config) : 0 < cfg.wordSize
```

`Batteries.Random.MersenneTwister.Config.zero_lt_stateSize` (theorem, [line 83](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Random/MersenneTwister.lean#L83))

```lean
theorem Config.zero_lt_stateSize (cfg : Config) : 0 < cfg.stateSize
```

`Batteries.Random.MersenneTwister.State` (structure, [line 87](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Random/MersenneTwister.lean#L87))

> Mersenne Twister State.

```lean
structure State (cfg : Config) where
  /-- Data for current state. -/
  data : Vector (BitVec cfg.wordSize) cfg.stateSize
  /-- Current data index. -/
  index : Fin cfg.stateSize
```

`Batteries.Random.MersenneTwister.Config.init` (definition, [line 94](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Random/MersenneTwister.lean#L94))

> Mersenne Twister initialization given an optional seed.

```lean
protected def Config.init (cfg : MersenneTwister.Config)
    (seed : BitVec cfg.wordSize := cfg.initSeed) : State cfg
```

`Batteries.Random.MersenneTwister.State.twist` (definition, [line 106](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Random/MersenneTwister.lean#L106))

> Apply the twisting transformation to the given state.

```lean
protected def State.twist (state : State cfg) : State cfg
```

`Batteries.Random.MersenneTwister.State.update` (definition, [line 116](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Random/MersenneTwister.lean#L116))

> Update the state by a number of generation steps (default 1).

```lean
protected def State.update (state : State cfg) : (steps : Nat := 1) → State cfg
```

`Batteries.Random.MersenneTwister.State.next` (definition, [line 121](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Random/MersenneTwister.lean#L121))

> Mersenne Twister iteration.

```lean
protected def State.next (state : State cfg) : BitVec cfg.wordSize × State cfg
```

`Batteries.Random.MersenneTwister.mt19937` (definition, [line 139](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Random/MersenneTwister.lean#L139))

> 32 bit Mersenne Twister (MT19937) configuration.

```lean
def mt19937 : Config
```

`Batteries.Random.MersenneTwister.mt19937_64` (definition, [line 151](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Random/MersenneTwister.lean#L151))

> 64 bit Mersenne Twister (MT19937-64) configuration.

```lean
def mt19937_64 : Config
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/Random/MersenneTwister.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Random/MersenneTwister.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Random.MersenneTwister.json)
