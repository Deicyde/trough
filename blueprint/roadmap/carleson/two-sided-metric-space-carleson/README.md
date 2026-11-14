# Two-sided Metric Space Carleson

We prove a variant of [metric space Carleson](../introduction/metric-space-carleson.md) for a two-sided Calderón–Zygmund kernel on the doubling metric measure space $(X,\rho,\mu,a)$, i.e. a one-sided Calderón–Zygmund kernel $K$ which additionally satisfies for all $x,x',y\in X$ with $x\neq y$ and $2\rho(x,x') \leq \rho(x,y)$,

$$
|K(x,y) - K(x',y)| \leq \left(\frac{\rho(x,x')}{\rho(x,y)}\right)^{\frac{1}{a}}\frac{2^{a^3}}{V(x,y)}.\qquad\text{(1)}
$$

By the additional regularity, we can weaken the assumption [(18)](../introduction/metric-space-carleson.md) to a family of operators that is easier to work with in applications. Namely, for $r > 0$, $x\in X$, and a bounded, measurable function $f:X\to{\mathbb{C}}$ supported on a set of finite measure, we define

$$
T_r f(x):= \int_{r\le\rho(x,y)} K(x,y) f(y) \, d\mu(y) = \int_{X\setminus B(x,r)} K(x,y) f(y) \, d\mu(y).\qquad\text{(2)}
$$

- [two-sided metric space Carleson](two-sided-metric-space-carleson.md)

For the remainder of this chapter, fix an integer $a\ge 4$, a doubling metric measure space $(X,\rho,\mu,a)$ and a two-sided Calderón–Zygmund kernel $K$ as in [two-sided metric space Carleson](two-sided-metric-space-carleson.md).

The following lemma is proved in Proof of Cotlar's Inequality.

- [nontangential-from-simple](nontangential-from-simple.md)

*Proof of two-sided metric space Carleson: shown with [two-sided metric space Carleson](two-sided-metric-space-carleson.md).*

The proof of [nontangential-from-simple](nontangential-from-simple.md) relies on the following auxiliary lemma which is proved in Calderón-Zygmund Decomposition.

- [Calderon-Zygmund Weak (1, 1)](calderon-zygmund-weak-1-1.md)

Throughout Calderón-Zygmund Decomposition and Proof of Cotlar's Inequality, for any measurable bounded function $w: X \to {\mathbb{C}}$, let $Mw: X \to [0, \infty)$ denote the corresponding Hardy–Littlewood maximal function defined in [Hardy–Littlewood](../proof-of-metric-space-carleson-overview/hardy-littlewood.md). Note: In some cases, a stronger formalization of [Hardy–Littlewood](../proof-of-metric-space-carleson-overview/hardy-littlewood.md) is used, where $w$ is not necessarily bounded. In particular it is applied to $T_rg$. Apart from [Hardy–Littlewood](../proof-of-metric-space-carleson-overview/hardy-littlewood.md), Calderón-Zygmund Decomposition and Proof of Cotlar's Inequality have no dependencies in the previous chapters.

## Proof of Cotlar's Inequality

- [geometric series estimate](geometric-series-estimate.md)
- [estimate x shift](estimate-x-shift.md)
- [Cotlar control](cotlar-control.md)
- [Cotlar sets](cotlar-sets.md)
- [Cotlar estimate](cotlar-estimate.md)

For the next Lemma, we define the following operation.

$$
T_{*}^r g(x):=\sup_{r\lt R}\sup_{x'\in B(x,R)} |T_R(g)(x')| \, .\qquad\text{(33)}
$$

- [simple nontangential operator](simple-nontangential-operator.md)

In order to pass from the one-sided truncation in $T_r$ and $T_{*}^r$ to the two-sided truncation in $T_*$, we show in the following two lemmas that the integral in [(16)](../introduction/README.md) can be exchanged for an integral over the difference of two balls.

- [small annulus](small-annulus.md)
- [nontangential operator boundary](nontangential-operator-boundary.md)

*Proof of nontangential-from-simple: shown with [nontangential-from-simple](nontangential-from-simple.md).*

## Calderón-Zygmund Decomposition

Calderón-Zygmund decomposition is a tool to extend $L^2$ bounds to $L^p$ bounds with $p<2$ or to the so-called weak $(1, 1)$ type endpoint bound. It is classical and can be found in (stein-book).

The following lemma is Theorem 3.1(b) in (stein-book). The proof uses [Hardy–Littlewood](../proof-of-metric-space-carleson-overview/hardy-littlewood.md).

- [Maximal theorem](maximal-theorem.md)
- [Lebesgue differentiation](lebesgue-differentiation.md)
- [Disjoint family countable](disjoint-family-countable.md)

The following lemma corresponds to Lemma 3.2 in (stein-book) with additional proof of the bounded intersection property taken from the proof of Proposition 7.1. It uses the following notation, which will be used throughout the rest of this section: whenever $B_j$ denotes a ball $B_j = B(x_j, r_j)$, define

$$
B_{n,j} = B(x_j, nr_j).
$$

- [Ball covering](ball-covering.md)

Most of the next lemma and its proof is taken from Theorem 4.2 in (stein-book).

- [Calderon Zygmund decomposition](calderon-zygmund-decomposition.md)

We use [Calderon Zygmund decomposition](calderon-zygmund-decomposition.md) to prove [Calderon-Zygmund Weak (1, 1)](calderon-zygmund-weak-1-1.md). For the remainder of this section, let $f:X\to{\mathbb{C}}$, $r>0$ and $\alpha>0$ as in [Calderon-Zygmund Weak (1, 1)](calderon-zygmund-weak-1-1.md). We define the constant

$$
c:= 2^{-a^3-12a-4}\qquad\text{(61)}
$$

and $\alpha' := c\alpha$. If $\alpha'\le\frac{1}{\mu(X)}\int |f|\,d\mu$, then we directly have

$$
\mu\left(\{x\in X: |T_r f(x)|>\alpha\}\right)\le \mu(X) \le \frac{1}{\alpha'} \int |f(y)|\, d\mu(y)
\le \frac{2^{a^3 + 19a}}{\alpha} \int |f(y)|\, d\mu(y),
$$

which proves [(12)](calderon-zygmund-weak-1-1.md). So assume from now on that $\alpha'>\frac{1}{\mu(X)}\int |f|\,d\mu$. Using [Calderon Zygmund decomposition](calderon-zygmund-decomposition.md) for $f$ and $\alpha'$, we obtain the decomposition

$$
f=g+b=g+\sum_j b_j
$$

such that the properties [(50)](calderon-zygmund-decomposition.md)-[(57)](calderon-zygmund-decomposition.md) are satisfied (with $\alpha'$ replacing $\alpha$). Let

$$
B_{3,j}=B(x_j, 3r_j)\qquad\text{(62)}
$$

as in the lemma. Then

$$
B_{6,j}=B(x_j, 6r_j)\qquad\text{(63)}
$$

is a ball with the same center as $B_{3,j}$ but with

$$
\mu(B_{6,j})\le 2^{a} \mu(B_{3,j}).\qquad\text{(64)}
$$

Let

$$
\Omega:=\bigcup_j B_{6,j}.\qquad\text{(65)}
$$

We deal with $T_rg$ and $T_rb$ separately in the following lemmas.

- [Estimate good](estimate-good.md)
- [Estimate bad partial](estimate-bad-partial.md)
- [Estimate F set](estimate-f-set.md)
- [Estimate bad](estimate-bad.md)

*Proof of Calderon-Zygmund Weak (1, 1): shown with [Calderon-Zygmund Weak (1, 1)](calderon-zygmund-weak-1-1.md).*
