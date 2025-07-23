"""Background worker logic for running bots."""

from .bots import aws_iam_monitor


def run_all():
    """Run all registered bots."""
    aws_iam_monitor.run()
