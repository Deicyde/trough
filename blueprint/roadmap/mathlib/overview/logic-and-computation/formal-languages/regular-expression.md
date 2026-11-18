# Regular expression

This is the definition of regular expressions. The names used here are meant to mirror the
[definition of a Kleene algebra](https://en.wikipedia.org/wiki/Kleene_algebra).
* `0` (`zero`) matches nothing
* `1` (`epsilon`) matches only the empty string
* `char a` matches only the string 'a'
* `star P` matches any finite concatenation of strings that match `P`
* `P + Q` (`plus P Q`) matches anything that matches `P` or `Q`
* `P * Q` (`comp P Q`) matches `x ++ y` if `x` matches `P` and `y` matches `Q`

```lean
RegularExpression.{u} (α : Type u) : Type u
```

## Depends on

Its statement uses no other concept on these lists.

## Sources

- [Mathlib documentation: `RegularExpression`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/RegularExpressions.html#RegularExpression)
- [Source of `RegularExpression` in Mathlib/Computability/RegularExpressions.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Computability/RegularExpressions.lean#L39)
- [Mathlib overview: Logic and computation › Formal languages](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L619)
