---
declaration: section
origin: cited
lean: Cslib.MachineLearning.Sequence.KalmanFilter.Belief, Cslib.MachineLearning.Sequence.KalmanFilter.Belief.Valid, Cslib.MachineLearning.Sequence.KalmanFilter.Belief.law, Cslib.MachineLearning.Sequence.KalmanFilter.predict, Cslib.MachineLearning.Sequence.KalmanFilter.gain, Cslib.MachineLearning.Sequence.KalmanFilter.update, Cslib.MachineLearning.Sequence.KalmanFilter.step, Cslib.MachineLearning.Sequence.KalmanFilter.predict_valid
statement: formalized
proof: formalized
---

# Kalman filter

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/kalman-filter/index.html).

## Gaussian belief

For an index type $n$, a belief about the state consists of a mean
$m \in \mathbb{R}^n$ and a covariance matrix $P$, an arbitrary real $n \times n$ matrix. It
describes the Gaussian distribution $N(m, P)$ when $P$ is positive semidefinite (the belief is
valid); for other matrices Mathlib's multivariate Gaussian is a junk value. Prediction with
positive semidefinite process noise, update with positive definite observation noise, and a filter
step with both preserve validity.

Formalized by `Cslib.MachineLearning.Sequence.KalmanFilter.Belief`, a structure declared in [CSLibExt/MachineLearning/Sequence/KalmanFilter.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Sequence/KalmanFilter.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/kalman-filter/index.html#belief).

## Valid Gaussian beliefs

A belief is valid when its covariance matrix is positive
semidefinite.

Formalized by `Cslib.MachineLearning.Sequence.KalmanFilter.Belief.Valid`, a definition declared in [CSLibExt/MachineLearning/Sequence/KalmanFilter.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Sequence/KalmanFilter.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/kalman-filter/index.html#valid).

## Law of a belief

The law of a belief with mean $m$ and covariance $P$ is Mathlib's
multivariate Gaussian measure $N(m, P)$ on $\mathbb{R}^n$. It is the Gaussian distribution with
mean $m$ and covariance $P$ when $P$ is positive semidefinite (the belief is valid); otherwise it
is the point mass at $m$.

Formalized by `Cslib.MachineLearning.Sequence.KalmanFilter.Belief.law`, a definition declared in [CSLibExt/MachineLearning/Sequence/KalmanFilter.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Sequence/KalmanFilter.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/kalman-filter/index.html#law).

## Kalman prediction

Given real $n \times n$ matrices $F$ and $Q$, the prediction of a
belief with mean $m$ and covariance $P$ is the belief with mean $F m$ and covariance
$F P F^\top + Q$. It models the dynamics $x' = F x + w$ with process noise $w \sim N(0, Q)$.

Formalized by `Cslib.MachineLearning.Sequence.KalmanFilter.predict`, a definition declared in [CSLibExt/MachineLearning/Sequence/KalmanFilter.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Sequence/KalmanFilter.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/kalman-filter/index.html#predict).

## Kalman gain

For a real $p \times n$ matrix $H$, a real $p \times p$ matrix $R$ and a
belief with covariance $P$, the Kalman gain is the real $n \times p$ matrix
$K = P H^\top (H P H^\top + R)^{-1}$, where the inverse is taken to be $0$ when
$H P H^\top + R$ is singular.

Formalized by `Cslib.MachineLearning.Sequence.KalmanFilter.gain`, a definition declared in [CSLibExt/MachineLearning/Sequence/KalmanFilter.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Sequence/KalmanFilter.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/kalman-filter/index.html#gain).

## Kalman filter update

Given a real $p \times n$ observation matrix $H$, a real $p \times p$
matrix $R$, an observation $y \in \mathbb{R}^p$ and a belief with mean $m$ and covariance $P$,
the updated belief has mean $m + K (y - H m)$ and covariance $(I - K H) P$, where
$K = P H^\top (H P H^\top + R)^{-1}$ is the Kalman gain and the matrix inverse is taken to be
$0$ when $H P H^\top + R$ is singular.

It corresponds to observing a state $x$ as $y = H x + v$ with Gaussian noise $v \sim N(0, R)$.

Formalized by `Cslib.MachineLearning.Sequence.KalmanFilter.update`, a definition declared in [CSLibExt/MachineLearning/Sequence/KalmanFilter.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Sequence/KalmanFilter.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/kalman-filter/index.html#update).

## Kalman filter step

Given real $n \times n$ matrices $F$ and $Q$, a real $p \times n$
matrix $H$, a real $p \times p$ matrix $R$ and an observation $y \in \mathbb{R}^p$, one filter
step sends a belief to the update, with $H$, $R$ and $y$, of its prediction with $F$ and $Q$.

Formalized by `Cslib.MachineLearning.Sequence.KalmanFilter.step`, a definition declared in [CSLibExt/MachineLearning/Sequence/KalmanFilter.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Sequence/KalmanFilter.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/kalman-filter/index.html#step).

## Prediction preserves validity

Let $F$ and $Q$ be real $n \times n$ matrices with $Q$
positive semidefinite. If a belief is valid, that is, its covariance $P$ is positive
semidefinite, then the predicted belief, with covariance $F P F^\top + Q$, is valid.

Formalized by `Cslib.MachineLearning.Sequence.KalmanFilter.predict_valid`, a theorem declared in [CSLibExt/MachineLearning/Sequence/KalmanFilter.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Sequence/KalmanFilter.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/kalman-filter/index.html#predict-valid).

## Schur form of the updated covariance

Let $H$ be a real $p \times n$ matrix, $R$ a real
$p \times p$ matrix and $y \in \mathbb{R}^p$, and let a belief have covariance $P$. Then the
covariance of the belief updated with $H$, $R$ and $y$ equals
$P - P H^\top (H P H^\top + R)^{-1} H P$. Here $M^{-1}$ is the matrix inverse, taken to be $0$
when $M$ is singular, so no invertibility is assumed.

With the Kalman gain $K = P H^\top (H P H^\top + R)^{-1}$ this says $(I - K H) P =
P - P H^\top (H P H^\top + R)^{-1} H P$.

Formalized by `Cslib.MachineLearning.Sequence.KalmanFilter.update_cov_eq`, a theorem declared in [CSLibExt/MachineLearning/Sequence/KalmanFilter.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Sequence/KalmanFilter.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/kalman-filter/index.html#update-cov-eq).

## The Kalman update preserves validity

Let $H$ be a real $p \times n$ matrix, $R$ a
symmetric positive definite real $p \times p$ matrix and $y \in \mathbb{R}^p$. If a belief is
valid, then the belief updated with $H$, $R$ and $y$ is valid.

Formalized by `Cslib.MachineLearning.Sequence.KalmanFilter.update_valid`, a theorem declared in [CSLibExt/MachineLearning/Sequence/KalmanFilter.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Sequence/KalmanFilter.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/kalman-filter/index.html#update-valid).

## A filter step preserves validity

Let $F$ and $Q$ be real $n \times n$ matrices with $Q$
positive semidefinite, $H$ a real $p \times n$ matrix, $R$ a positive definite real $p \times p$
matrix and $y \in \mathbb{R}^p$. If a belief is valid (its covariance is positive semidefinite),
then so is the belief obtained from it by one filter step with $F$, $Q$, $H$, $R$ and the
observation $y$.

Formalized by `Cslib.MachineLearning.Sequence.KalmanFilter.step_valid`, a theorem declared in [CSLibExt/MachineLearning/Sequence/KalmanFilter.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Sequence/KalmanFilter.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/kalman-filter/index.html#step-valid).

## The predict step is exact

Let $x$ and $w$ be measurable, independent random vectors in
$\mathbb{R}^n$ on a probability space. If $x$ has the law $N(m, P)$ of a belief with mean $m$ and
positive semidefinite covariance $P$, and $w$ has law $N(0, Q)$ with $Q$ positive semidefinite,
then for every real $n \times n$ matrix $F$ the random vector $F x + w$ has the law of the
predicted belief, $N(F m, F P F^\top + Q)$.

Formalized by `Cslib.MachineLearning.Sequence.KalmanFilter.map_predict`, a theorem declared in [CSLibExt/MachineLearning/Sequence/KalmanFilter.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Sequence/KalmanFilter.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/kalman-filter/index.html#map-predict).

## The update step is the exact posterior

Let $x$ be a measurable random vector in
$\mathbb{R}^n$ and $v$ a measurable random vector in $\mathbb{R}^p$ on a probability space, with
$x$ independent of $v$. Suppose $x$ has the law $N(m, P)$ of a belief with mean $m$ and positive
semidefinite covariance $P$, and $v$ has law $N(0, R)$ with $R$ positive semidefinite. Let $H$ be
a real $p \times n$ matrix with $H P H^\top + R$ invertible, and put $Y = H x + v$. Then for
almost every $y$ with respect to the law of $Y$, the conditional distribution of $x$ given
$Y = y$ is the law of the belief obtained from $(m, P)$ by the update with $H$, $R$ and the
observation $y$.

Formalized by `Cslib.MachineLearning.Sequence.KalmanFilter.condDistrib_update`, a theorem declared in [CSLibExt/MachineLearning/Sequence/KalmanFilter.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Sequence/KalmanFilter.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/kalman-filter/index.html#cond-distrib-update).

## One filter step is the exact posterior

Let $x$ and $w$ be measurable random vectors in
$\mathbb{R}^n$ and $v$ a measurable random vector in $\mathbb{R}^p$ on a probability space, with
$x$ independent of $w$ and the pair $(x, w)$ independent of $v$. Suppose $x$ has the law
$N(m, P)$ of a belief with mean $m$ and positive semidefinite covariance $P$, $w$ has law
$N(0, Q)$ and $v$ has law $N(0, R)$, with $Q$ and $R$ positive semidefinite. Let $F$ be a real
$n \times n$ matrix and $H$ a real $p \times n$ matrix with $H (F P F^\top + Q) H^\top + R$
invertible, and put $x' = F x + w$ and $Y = H x' + v$. Then for almost every $y$ with respect to
the law of $Y$, the conditional distribution of $x'$ given $Y = y$ is the law of the belief
obtained from $(m, P)$ by one filter step with $F$, $Q$, $H$, $R$ and the observation $y$.

Formalized by `Cslib.MachineLearning.Sequence.KalmanFilter.condDistrib_step`, a theorem declared in [CSLibExt/MachineLearning/Sequence/KalmanFilter.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Sequence/KalmanFilter.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/kalman-filter/index.html#cond-distrib-step).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kalman filter](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/kalman-filter/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/kalman-filter)
