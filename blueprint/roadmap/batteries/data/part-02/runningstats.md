---
catalog: module
lean: Batteries.RunningStats, Batteries.RunningStats.push, Batteries.RunningStats.variance, Batteries.RunningStats.sampleVariance, Batteries.RunningStats.standardDeviation, Batteries.RunningStats.sampleStandardDeviation
statement: formalized
proof: formalized
---

# Running Statistics

`Batteries.Data.RunningStats`, in [Batteries/Data/RunningStats.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/RunningStats.lean), by François G. Dorais.

> This module implements Welford's one-pass algorithm for calculating the mean and
> standard deviation of a sample or a population. The advantage of this algorithm is
> This module implements Welford's one-pass algorithm for calculating the mean,
> variance and standard deviation of a sample or a population. The advantage of
> this algorithm is that it is not necessary to store the data.
>
> The algorithm uses the recurrence formulas for the mean `μ`, variance `σ²`
> and the sample variance `s²`:
> ```
>   μₖ = μₖ₋₁ + (xₖ − μₖ₋₁)/k
>   σ²ₖ = σ²ₖ₋₁*(k-1)/k + (xₖ − μₖ₋₁)*(xₖ − μₖ)/k
>   s²ₖ = s²ₖ₋₁*(k-2)/(k-1) + (xₖ - μₖ₋₁)²/k
> ```
> To improve performance, Welford's algorithm keeps track of the two running
> quantities:
> ```
>   Mₖ = Mₖ₋₁ + (xₖ - Mₖ₋₁)/k
>   Sₖ = Sₖ₋₁ + (xₖ - Mₖ₋₁)*(xₖ - Mₖ)
> ```
> Then: `μₖ = Mₖ`, `σ²ₖ = Sₖ/k`, `s²ₖ = Sₖ/(k-1)`.

`Batteries.RunningStats` (structure, [line 38](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/RunningStats.lean#L38))

> Compute running statistics of a data stream using Welford's algorithm.

```lean
public structure RunningStats where
  /-- Initialize running statistics. -/
  init ::
  /-- Number of data points, -/
  count : Nat := 0
  /-- Mean of data points. -/
  mean : Float := 0.0
  /-- Variance of data points times the number of data points. -/
  var : Float := 0.0
```

`Batteries.RunningStats.push` (definition, [line 52](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/RunningStats.lean#L52))

> Add a new data point to running statistics.

```lean
public def push (data : Float) (s : RunningStats) : RunningStats
```

`Batteries.RunningStats.variance` (definition, [line 60](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/RunningStats.lean#L60))

> Variance of running data stream (population variance).

```lean
public def variance (s : RunningStats) : Float
```

`Batteries.RunningStats.sampleVariance` (definition, [line 65](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/RunningStats.lean#L65))

> Unbiased variance of running data stream (sample variance).

```lean
public def sampleVariance (s : RunningStats) : Float
```

`Batteries.RunningStats.standardDeviation` (definition, [line 70](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/RunningStats.lean#L70))

> Standard deviation of running data stream (square-root of population variance).

```lean
public def standardDeviation (s : RunningStats) : Float
```

`Batteries.RunningStats.sampleStandardDeviation` (definition, [line 75](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/RunningStats.lean#L75))

> Sample standard deviation of running data stream (square root of sample variance).

```lean
public def sampleStandardDeviation (s : RunningStats) : Float
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/RunningStats.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/RunningStats.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Data.RunningStats.json)
