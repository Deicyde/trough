---
declaration: lemma
origin: cited
lean: simple_nontangential_operator, lowerSemicontinuous_simpleNontangentialOperator
statement: formalized
proof: formalized
---

# simple nontangential operator

Assume that [(3)](two-sided-metric-space-carleson.md) holds. For every $r>0$ and every bounded measurable function $g$ supported on a set of finite measure the function $T_{*}^r g$ is lower-semicontinuous and we have

$$
\|T_{*}^rg\|_2\le 2^{a^3+24a+6}\|g\|_2,\qquad\text{(34)}
$$

## Depends on

- [Hardy–Littlewood](../proof-of-metric-space-carleson-overview/hardy-littlewood.md)
- [Cotlar estimate](cotlar-estimate.md)

## Proof

For a fixed $\lambda$ we note that (rewriting $x'\in B(x,R)$ as $x\in B(x',R)$):

$$
\{x : T_{*}^r g(x) > \lambda\} = \bigcup_{r\lt R}\bigcup_{\{x':|T_R(g)(x')|>\lambda\}} B(x',R)
$$

The right-hand side is open, hence $T_{*}^r g$ is lower-semicontinuous by definition.

For the second part, with [estimate x shift](estimate-x-shift.md) and the triangle inequality, we estimate for every $x\in X$

$$
T_{*}^r g(x)
\le 2^{a^3 + 2a + 2} Mg(x)+\sup_{r\lt R} |T_R(g)(x)|\, .
$$

Using further [Cotlar estimate](cotlar-estimate.md), we estimate

$$
T_{*}^r g(x)
\le 2^{a^3+2a+2}Mg(x) + 2^{a^3+20a+3}Mg(x) + 2^{2}M(T_rg)(x)\, .
$$

Taking the $L^2$ norm and using [Hardy–Littlewood](../proof-of-metric-space-carleson-overview/hardy-littlewood.md) with $a=4$ and $p_2=2$ and $p_1=1$ , we obtain

$$
\|T_{*}^r g\|_2
\le 2^{a^3+20a+4} \|Mg\|_2 + 2^{2}\|M(T_rg)\|_2
$$

$$
\le 2^{a^3+24a+5} \|g\|_2 + 2^{4a+3}\|T_r g\|_2\, .
$$

Applying [(3)](two-sided-metric-space-carleson.md) gives

$$
\|T_{*}^r g\|_2\le 2^{a^3+24a+5}\|g\|_2 + 2^{a^3+4a+3}\|g\|_2\, .
$$

This shows (34) and completes the proof of the inequality.

## Lean

Formalized as [`simple_nontangential_operator`](https://fpvandoorn.github.io/carleson/docs/find/#doc/simple_nontangential_operator), [`lowerSemicontinuous_simpleNontangentialOperator`](https://fpvandoorn.github.io/carleson/docs/find/#doc/lowerSemicontinuous_simpleNontangentialOperator).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 7380](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L7380)
